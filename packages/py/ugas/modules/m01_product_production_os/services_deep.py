# GENERATED-DEEP-PREPROGRAMMED
"""M01 orchestration: graph lifecycle, exactly-once transitions, invalidation and execution planning.

The transition service consumes the foundation's idempotency boundary so a committed sequential replay cannot
apply a domain mutation twice. The invalidation service emits kernel Evidence Graph states, so M01 carries no
proof state of its own.
"""
from __future__ import annotations

from dataclasses import replace
from typing import Any

from ugas.foundation.contracts import ProductionGraph, content_fingerprint_of
from ugas.foundation.idempotency import IdempotencyStore, execute_once
from ugas.foundation.invalidation import bridge_proof_invalidation, downstream_invalidation

from .contracts import InvalidationRequest, PlanningRequest, TransitionRequest
from .domain import apply_transition, assert_project_scope, execution_plan
from .errors import ValidationError


def _planning_input(request: Any) -> tuple[str, ProductionGraph]:
    """Accept either the typed M01 PlanningRequest or a bare canonical ProductionGraph.

    The bare form exists so the S01 golden slice can drive this port without foundation importing M01: a
    ProductionGraph already carries its project_id, so accepting it loses nothing.
    """
    if isinstance(request, PlanningRequest):
        return request.project_id, request.graph
    if isinstance(request, ProductionGraph):
        return request.project_id, request
    raise ValidationError("expected a PlanningRequest or a canonical ProductionGraph")


def _resign(graph: ProductionGraph) -> ProductionGraph:
    """Return the graph with a fingerprint derived from its new content."""
    return replace(graph, fingerprint=content_fingerprint_of(graph))


class ProductionGraphService:
    """PREPROGRAMMED orchestration boundary for M01."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> dict[str, Any]:
        """Validate a production graph and report its deterministic shape."""
        project_id, graph = _planning_input(request)
        assert_project_scope(project_id, graph)
        return {
            "graph_id": graph.id,
            "nodes": len(graph.nodes),
            "edges": len(graph.edges),
            "execution_plan": execution_plan(graph),
            "graph_fingerprint": content_fingerprint_of(graph),
        }


class StateTransitionService:
    """PREPROGRAMMED orchestration boundary for M01."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> tuple[ProductionGraph, bool]:
        """Apply one node transition exactly once, keyed by (project, idempotency key, request fingerprint).

        Returns (graph, executed). A sequential replay of a committed request returns the committed graph
        without re-applying the mutation. Reusing the key with a different request fingerprint is a conflict.
        """
        if not isinstance(request, TransitionRequest):
            raise ValidationError("StateTransitionService requires a TransitionRequest")
        assert_project_scope(request.project_id, request.graph)
        store: IdempotencyStore[ProductionGraph] | None = self._ports.get("store")
        if store is None:
            raise ValidationError("StateTransitionService requires an idempotency store port")

        async def mutation() -> ProductionGraph:
            return _resign(apply_transition(request.graph, request.node_id, request.before, request.after))

        return await execute_once(
            store,
            project_id=request.project_id,
            key=request.idempotency_key,
            request_fingerprint=request.request_fingerprint,
            mutation=mutation,
        )


class InvalidationService:
    """PREPROGRAMMED orchestration boundary for M01."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> dict[str, Any]:
        """Compute the causal invalidation cone and bridge it onto the canonical kernel Evidence Graph.

        Only the changed dependency cone is invalidated; unaffected siblings carry forward. The event is emitted
        to the EvidenceSink port when one is supplied.
        """
        if not isinstance(request, InvalidationRequest):
            raise ValidationError("InvalidationService requires an InvalidationRequest")
        assert_project_scope(request.project_id, request.graph)
        affected = downstream_invalidation(request.graph, request.changed_node_ids)
        evidence = bridge_proof_invalidation(request.graph, request.changed_node_ids, self._ports.get("proof_nodes", ()))
        event = {
            "project_id": request.project_id,
            "changed_node_ids": tuple(request.changed_node_ids),
            "affected_node_ids": affected,
            "invalidated": tuple(n.id for n in evidence.nodes if n.state.value == "invalidated"),
            "carried_forward": tuple(n.id for n in evidence.nodes if n.state.value == "carry_forward"),
        }
        sink = self._ports.get("evidence_sink")
        if sink is not None:
            await sink.emit(event)
        return event


class ExecutionPlanningService:
    """PREPROGRAMMED orchestration boundary for M01."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> dict[str, Any]:
        """Produce the deterministic execution plan for a validated graph."""
        project_id, graph = _planning_input(request)
        assert_project_scope(project_id, graph)
        return {"plan": execution_plan(graph), "project_id": project_id}


# CODEX-TASK[M01-ProductionGraphService] / [M01-StateTransitionService] / [M01-InvalidationService]
#          / [M01-ExecutionPlanningService]
# DONE: all four services implemented. Transitions are exactly-once through the foundation idempotency boundary;
#       invalidation emits kernel Evidence Graph states and never declares its own proof taxonomy.
