from ugas.foundation.contracts import (
    AssetDNA, GraphEdge, GraphNode, ModelProfile, NodeState, ProductionGraph,
    QualificationState, ResourceEnvelope, KnowledgeState,
)
from ugas.foundation.invariants import assert_dna_derivative, assert_graph, assert_legal_transition
from ugas.foundation.routing import TaskRequirements, choose_route


def test_illegal_transition_is_rejected():
    try:
        assert_legal_transition(NodeState.PLANNED, NodeState.ACCEPTED)
    except ValueError:
        return
    raise AssertionError("illegal transition must fail")


def test_cycle_is_rejected():
    a = GraphNode("a", 1, "fa", "p", NodeState.READY, "ir-a")
    b = GraphNode("b", 1, "fb", "p", NodeState.READY, "ir-b")
    graph = ProductionGraph("g", 1, "fg", "p", (a, b), (GraphEdge("a", "b", "depends"), GraphEdge("b", "a", "depends")))
    try:
        assert_graph(graph)
    except ValueError:
        return
    raise AssertionError("cycle must fail")


def test_locked_dna_trait_is_preserved():
    canonical = AssetDNA("dna", 1, "f1", "p", "hero", {"face":"A"}, {"hair":"black"})
    derivative = AssetDNA("dna-v", 2, "f2", "p", "hero", {"face":"A"}, {"hair":"silver"}, "f1")
    assert_dna_derivative(canonical, derivative)


def test_route_is_deterministic_and_hardware_bounded():
    hw = ResourceEnvelope("hw", 1, "fh", KnowledgeState.KNOWN, "gpu", 8192, 7000, 24000, 1)
    req = TaskRequirements("rq", {"image":1.0}, {"image":0.7})
    a = ModelProfile("a", 1, "fa", "model-a", QualificationState.QUALIFIED, {"image":0.9}, 6000)
    b = ModelProfile("b", 1, "fb", "model-b", QualificationState.QUALIFIED, {"image":0.9}, 6000)
    assert choose_route([b,a], req, hw).model.model_key == "model-a"
    assert choose_route([a,b], req, hw).model.model_key == "model-a"


def test_unqualified_model_cannot_route():
    hw = ResourceEnvelope("hw", 1, "fh", KnowledgeState.KNOWN, "gpu", 8192, 7000, 24000, 1)
    req = TaskRequirements("rq", {"image":1.0}, {"image":0.1})
    model = ModelProfile("x", 1, "fx", "candidate", QualificationState.CANDIDATE, {"image":1.0}, 1000)
    try:
        choose_route([model], req, hw)
    except ValueError:
        return
    raise AssertionError("candidate model must not route production")


# CODEX-TASK[S01-TEST-EXPANSION]
# DONE: canonical serialization/fingerprint tests live in test_foundation_canonical.py, diamond
#       invalidation and kernel proof-bridge tests in test_foundation_lifecycle.py, idempotent mutation
#       in test_foundation_idempotency.py, unknown/degraded hardware and routing in
#       test_foundation_routing.py, and the Golden foundation integration in test_s01_golden_path.py.
#       The five original tests here are retained unchanged.
# Add canonical serialization/fingerprint, lock-preserving IR migration, diamond invalidation,
# unknown/degraded hardware, idempotent mutation and Golden foundation integration tests.
