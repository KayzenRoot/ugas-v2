"""A1 focused M01 lifecycle/service tests: transitions, exactly-once replay, invalidation, planning."""
import asyncio

from ugas.foundation.contracts import GraphEdge, GraphNode, NodeState, ProductionGraph
from ugas.foundation.idempotency import IdempotencyRecord
from ugas.kernel.evidence_graph import EvidenceNode, ProofState
from ugas.modules.m01_product_production_os.contracts import (
    InvalidationRequest, PlanningRequest, TransitionRequest,
)
from ugas.modules.m01_product_production_os.domain import apply_transition, execution_plan
from ugas.modules.m01_product_production_os.errors import StaleState, ValidationError
from ugas.modules.m01_product_production_os.services_deep import (
    ExecutionPlanningService, InvalidationService, ProductionGraphService, StateTransitionService,
)
import pytest


def run(coro):
    return asyncio.run(coro)


class FakeStore:
    def __init__(self):
        self.records = {}

    async def get(self, project_id, key):
        return self.records.get((project_id, key))

    async def put_started(self, record):
        self.records[(record.project_id, record.key)] = record

    async def put_committed(self, record):
        self.records[(record.project_id, record.key)] = record

    async def put_failed(self, record):
        self.records[(record.project_id, record.key)] = record


class FakeSink:
    def __init__(self):
        self.events = []

    async def emit(self, event):
        self.events.append(event)


def _node(node_id, state=NodeState.READY):
    return GraphNode(node_id, 1, f"f-{node_id}", "p", state, f"ir-{node_id}")


def _diamond(states=None):
    states = states or {}
    nodes = tuple(_node(n, states.get(n, NodeState.READY)) for n in ("a", "b", "c", "d"))
    edges = (GraphEdge("a", "b", "depends"), GraphEdge("a", "c", "depends"),
             GraphEdge("b", "d", "depends"), GraphEdge("c", "d", "depends"))
    return ProductionGraph("g", 1, "fg", "p", nodes, edges)


def _transition(graph, node_id="a", before=NodeState.READY, after=NodeState.RUNNING, key="k1", rf="rf1"):
    return TransitionRequest("p", graph, node_id, before, after, key, rf)


def test_apply_transition_moves_the_node_and_reseals_fingerprint():
    updated = apply_transition(_diamond(), "a", NodeState.READY, NodeState.RUNNING)
    assert {n.id: n.state for n in updated.nodes}["a"] is NodeState.RUNNING
    assert updated.fingerprint != "fg"


def test_illegal_transition_is_rejected():
    with pytest.raises(ValueError):
        apply_transition(_diamond(), "a", NodeState.READY, NodeState.ACCEPTED)


def test_stale_view_is_reported_as_stale_state_not_retried():
    graph = _diamond({"a": NodeState.RUNNING})
    with pytest.raises(StaleState) as excinfo:
        apply_transition(graph, "a", NodeState.READY, NodeState.CANDIDATE)
    assert excinfo.value.kind.value == "stale_state"
    assert excinfo.value.retryable is False, "a stale view needs reconciliation, not a blind retry"


def test_unknown_node_fails_closed():
    with pytest.raises(ValidationError):
        apply_transition(_diamond(), "ghost", NodeState.READY, NodeState.RUNNING)


def test_cyclic_graph_is_rejected():
    nodes = (_node("a"), _node("b"))
    edges = (GraphEdge("a", "b", "depends"), GraphEdge("b", "a", "depends"))
    with pytest.raises(ValueError):
        execution_plan(ProductionGraph("g", 1, "fg", "p", nodes, edges))


def test_execution_plan_is_topological_and_order_independent():
    assert execution_plan(_diamond()) == ("a", "b", "c", "d")


def test_execution_plan_excludes_settled_nodes():
    graph = _diamond({"a": NodeState.ACCEPTED})
    plan = execution_plan(graph)
    assert "a" not in plan, "an accepted node must not be scheduled again"
    assert set(plan) <= {"b", "c", "d"}


def test_transition_executes_once_under_sequential_replay():
    store, graph = FakeStore(), _diamond()
    service = StateTransitionService(store=store)
    first_graph, executed_first = run(service.execute(_transition(graph)))
    second_graph, executed_second = run(service.execute(_transition(graph)))
    assert executed_first is True and executed_second is False
    assert first_graph.fingerprint == second_graph.fingerprint, "replay returns the committed graph"


def test_transition_key_reuse_with_different_fingerprint_conflicts():
    from ugas.foundation.idempotency import IdempotencyConflict

    store, graph = FakeStore(), _diamond()
    service = StateTransitionService(store=store)
    run(service.execute(_transition(graph)))
    with pytest.raises(IdempotencyConflict):
        run(service.execute(_transition(graph, rf="rf-other")))


def test_transition_requires_a_store_port():
    with pytest.raises(ValidationError):
        run(StateTransitionService().execute(_transition(_diamond())))


def test_cross_project_request_is_rejected():
    graph = _diamond()
    request = TransitionRequest("other", graph, "a", NodeState.READY, NodeState.RUNNING, "k", "rf")
    with pytest.raises(ValidationError):
        run(StateTransitionService(store=FakeStore()).execute(request))


def _proofs():
    return (
        EvidenceNode("a", "p", "a", "identity", ProofState.PROVEN, "m01", (), "proof:a"),
        EvidenceNode("b", "p", "b", "temporal", ProofState.PROVEN, "m01", ("a",), "proof:b"),
        EvidenceNode("c", "p", "c", "voice", ProofState.PROVEN, "m01", (), "proof:c"),
        EvidenceNode("d", "p", "d", "delivery", ProofState.PROVEN, "m01", ("b", "c"), "proof:d"),
    )


def test_invalidation_limits_scope_and_emits_canonical_states():
    sink = FakeSink()
    event = run(InvalidationService(proof_nodes=_proofs(), evidence_sink=sink).execute(
        InvalidationRequest("p", _diamond(), ("b",))))
    assert event["affected_node_ids"] == ("b", "d")
    assert event["invalidated"] == ("b", "d")
    assert event["carried_forward"] == ("a", "c"), "unrelated siblings must carry forward"
    assert sink.events == [event]


def test_invalidation_without_sink_still_returns_the_event():
    event = run(InvalidationService(proof_nodes=_proofs()).execute(InvalidationRequest("p", _diamond(), ("a",))))
    assert event["affected_node_ids"] == ("a", "b", "c", "d")


def test_graph_service_reports_shape_and_plan():
    report = run(ProductionGraphService().execute(PlanningRequest("p", _diamond())))
    assert report["nodes"] == 4 and report["edges"] == 4
    assert report["execution_plan"] == ("a", "b", "c", "d")


def test_planning_service_is_deterministic():
    service = ExecutionPlanningService()
    first = run(service.execute(PlanningRequest("p", _diamond())))
    second = run(service.execute(PlanningRequest("p", _diamond())))
    assert first == second
