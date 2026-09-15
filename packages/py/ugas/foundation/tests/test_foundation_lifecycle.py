"""A1 graph lifecycle, invalidation cone and kernel proof-bridge tests for the S01 foundation."""
from ugas.foundation.contracts import GraphEdge, GraphNode, NodeState, ProductionGraph
from ugas.foundation.invalidation import bridge_proof_invalidation, downstream_invalidation, unaffected_node_ids
from ugas.foundation.invariants import assert_graph, assert_legal_transition
from ugas.kernel.evidence_graph import EvidenceGraph, EvidenceNode, ProofState, validate_graph
import pytest


def _node(node_id, state=NodeState.READY, ir_ref=None):
    return GraphNode(node_id, 1, f"f-{node_id}", "p", state, ir_ref or f"ir-{node_id}")


def _diamond():
    """a -> b, a -> c, b -> d, c -> d. A change at a reaches d; a change at b must not reach c."""
    nodes = (_node("a"), _node("b"), _node("c"), _node("d"))
    edges = (GraphEdge("a", "b", "depends"), GraphEdge("a", "c", "depends"),
             GraphEdge("b", "d", "depends"), GraphEdge("c", "d", "depends"))
    return ProductionGraph("g", 1, "fg", "p", nodes, edges)


def test_illegal_transition_is_rejected():
    with pytest.raises(ValueError):
        assert_legal_transition(NodeState.PLANNED, NodeState.ACCEPTED)


def test_legal_transition_is_accepted():
    assert_legal_transition(NodeState.PLANNED, NodeState.READY)
    assert_legal_transition(NodeState.CANDIDATE, NodeState.ACCEPTED)


def test_cycle_is_rejected():
    a, b = _node("a"), _node("b")
    graph = ProductionGraph("g", 1, "fg", "p", (a, b), (GraphEdge("a", "b", "depends"), GraphEdge("b", "a", "depends")))
    with pytest.raises(ValueError):
        assert_graph(graph)


def test_cross_project_node_is_rejected():
    graph = ProductionGraph("g", 1, "fg", "p", (GraphNode("a", 1, "fa", "other", NodeState.READY, "ir"),), ())
    with pytest.raises(ValueError):
        assert_graph(graph)


def test_diamond_invalidation_reaches_the_join():
    assert downstream_invalidation(_diamond(), {"a"}) == ("a", "b", "c", "d")


def test_sibling_is_not_invalidated():
    """A change at b must invalidate b and d, but never the sibling c."""
    assert downstream_invalidation(_diamond(), {"b"}) == ("b", "d")
    assert "c" in unaffected_node_ids(_diamond(), {"b"})


def test_leaf_change_does_not_touch_ancestors():
    assert downstream_invalidation(_diamond(), {"d"}) == ("d",)
    assert unaffected_node_ids(_diamond(), {"d"}) == ("a", "b", "c")


def test_invalidation_is_repeat_deterministic():
    graph = _diamond()
    assert downstream_invalidation(graph, {"a"}) == downstream_invalidation(graph, {"a"})
    assert downstream_invalidation(graph, {"c", "b"}) == ("b", "c", "d")


def test_unknown_changed_node_fails_closed():
    with pytest.raises(ValueError):
        downstream_invalidation(_diamond(), {"ghost"})


def _proofs():
    return (
        EvidenceNode("a", "p", "a", "identity", ProofState.PROVEN, "m01", (), "proof:a"),
        EvidenceNode("b", "p", "b", "temporal", ProofState.PROVEN, "m01", ("a",), "proof:b"),
        EvidenceNode("c", "p", "c", "voice", ProofState.PROVEN, "m01", (), "proof:c"),
        EvidenceNode("d", "p", "d", "delivery", ProofState.PROVEN, "m01", ("b", "c"), "proof:d"),
    )


def test_proof_bridge_uses_canonical_kernel_states():
    bridged = bridge_proof_invalidation(_diamond(), {"b"}, _proofs())
    validate_graph(bridged)
    states = {node.id: node.state for node in bridged.nodes}
    assert all(isinstance(state, ProofState) for state in states.values())
    assert states["b"] is ProofState.INVALIDATED and states["d"] is ProofState.INVALIDATED
    assert states["a"] is ProofState.CARRY_FORWARD and states["c"] is ProofState.CARRY_FORWARD


def test_proof_bridge_clears_evidence_on_invalidated_nodes_only():
    bridged = bridge_proof_invalidation(_diamond(), {"b"}, _proofs())
    by_id = {node.id: node for node in bridged.nodes}
    assert by_id["b"].evidence_ref is None
    assert by_id["a"].evidence_ref == "proof:a"


def test_proof_bridge_never_invents_missing_proofs():
    """A node with no supplied proof is absent; it is not fabricated as PROVEN."""
    bridged = bridge_proof_invalidation(_diamond(), {"b"}, _proofs()[:2])
    assert {node.id for node in bridged.nodes} == {"a", "b"}


def test_proof_bridge_unknown_state_is_rejected_not_coerced():
    bad = (EvidenceNode("a", "p", "a", "identity", "not-a-proof-state", "m01", (), "proof:a"),)
    with pytest.raises(ValueError):
        bridge_proof_invalidation(_diamond(), {"a"}, bad)
