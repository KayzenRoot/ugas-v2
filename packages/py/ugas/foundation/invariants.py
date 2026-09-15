from __future__ import annotations

"""Pure executable invariants for the S01 foundation."""
from collections import defaultdict, deque
from typing import Iterable, Mapping

from .contracts import AssetDNA, GraphEdge, ModelProfile, NodeState, ProductionGraph, QualificationState, ResourceEnvelope


LEGAL_TRANSITIONS: Mapping[NodeState, frozenset[NodeState]] = {
    NodeState.PLANNED: frozenset({NodeState.READY, NodeState.BLOCKED}),
    NodeState.READY: frozenset({NodeState.RUNNING, NodeState.BLOCKED, NodeState.INVALIDATED}),
    NodeState.RUNNING: frozenset({NodeState.CANDIDATE, NodeState.REJECTED, NodeState.BLOCKED}),
    NodeState.CANDIDATE: frozenset({NodeState.ACCEPTED, NodeState.REJECTED, NodeState.INVALIDATED}),
    NodeState.ACCEPTED: frozenset({NodeState.INVALIDATED}),
    NodeState.REJECTED: frozenset({NodeState.READY, NodeState.INVALIDATED}),
    NodeState.BLOCKED: frozenset({NodeState.READY, NodeState.INVALIDATED}),
    NodeState.INVALIDATED: frozenset({NodeState.READY, NodeState.BLOCKED}),
}


def assert_legal_transition(before: NodeState, after: NodeState) -> None:
    if after not in LEGAL_TRANSITIONS[before]:
        raise ValueError(f"illegal node transition: {before.value} -> {after.value}")


def assert_acyclic(node_ids: Iterable[str], edges: Iterable[GraphEdge]) -> None:
    ids = set(node_ids)
    incoming = {node_id: 0 for node_id in ids}
    outgoing: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        if edge.source not in ids or edge.target not in ids:
            raise ValueError("edge references unknown node")
        outgoing[edge.source].append(edge.target)
        incoming[edge.target] += 1
    queue = deque(sorted(node_id for node_id, degree in incoming.items() if degree == 0))
    visited = 0
    while queue:
        current = queue.popleft(); visited += 1
        for target in sorted(outgoing[current]):
            incoming[target] -= 1
            if incoming[target] == 0:
                queue.append(target)
    if visited != len(ids):
        raise ValueError("production graph contains a cycle")


def assert_graph(graph: ProductionGraph) -> None:
    ids = [node.id for node in graph.nodes]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate graph node id")
    if any(node.project_id != graph.project_id for node in graph.nodes):
        raise ValueError("cross-project node in production graph")
    assert_acyclic(ids, graph.edges)


def assert_dna_derivative(canonical: AssetDNA, derivative: AssetDNA) -> None:
    if canonical.project_id != derivative.project_id:
        raise ValueError("cross-project DNA derivative")
    if canonical.canonical_asset_id != derivative.canonical_asset_id:
        raise ValueError("canonical asset identity changed")
    for key, value in canonical.locked_traits.items():
        if derivative.locked_traits.get(key) != value:
            raise ValueError(f"locked DNA trait changed: {key}")
    if derivative.parent_fingerprint != canonical.fingerprint:
        raise ValueError("derivative must reference canonical parent fingerprint")


def model_fits_hardware(model: ModelProfile, hardware: ResourceEnvelope) -> bool:
    if model.qualification not in {QualificationState.QUALIFIED, QualificationState.PROMOTED}:
        return False
    if model.min_vram_mb is None:
        return True
    if hardware.vram_available_mb is None:
        return False
    return model.min_vram_mb <= hardware.vram_available_mb


# CODEX-TASK[S01-INVALIDATION]
# WHAT: add deterministic downstream invalidation traversal from changed graph nodes.
# INPUT: validated ProductionGraph + changed node ids.
# OUTPUT: stable tuple of affected node ids excluding unaffected ancestors/siblings.
# INVARIANTS: deterministic order; accepted proof invalidated only when dependency cone intersects change.
# ERRORS: unknown changed node fails explicitly.
# TEST: diamond graph, sibling isolation, repeated call determinism.
# DONE: traversal tests pass and no persistence/provider dependency is introduced.
