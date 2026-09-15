from __future__ import annotations

"""Deterministic downstream invalidation for M01 proof/test economy."""
from collections import defaultdict, deque
from typing import Iterable

from ugas.kernel.evidence_graph import EvidenceGraph, EvidenceNode, ProofState

from .contracts import ProductionGraph
from .invariants import assert_graph


def downstream_invalidation(graph: ProductionGraph, changed_node_ids: Iterable[str]) -> tuple[str, ...]:
    assert_graph(graph)
    known = {node.id for node in graph.nodes}
    changed = set(changed_node_ids)
    unknown = changed - known
    if unknown:
        raise ValueError(f"unknown changed nodes: {sorted(unknown)}")

    outgoing: dict[str, list[str]] = defaultdict(list)
    for edge in graph.edges:
        outgoing[edge.source].append(edge.target)
    for targets in outgoing.values():
        targets.sort()

    affected = set(changed)
    queue = deque(sorted(changed))
    while queue:
        current = queue.popleft()
        for target in outgoing[current]:
            if target not in affected:
                affected.add(target)
                queue.append(target)
    return tuple(sorted(affected))


def unaffected_node_ids(graph: ProductionGraph, changed_node_ids: Iterable[str]) -> tuple[str, ...]:
    affected = set(downstream_invalidation(graph, changed_node_ids))
    return tuple(sorted(node.id for node in graph.nodes if node.id not in affected))


def bridge_proof_invalidation(
    graph: ProductionGraph,
    changed_node_ids: Iterable[str],
    nodes: Iterable[EvidenceNode],
) -> EvidenceGraph:
    """Map a graph delta onto the canonical kernel Evidence Graph.

    Affected nodes become INVALIDATED and everyone else CARRY_FORWARD. Proof state, error kinds and the graph
    fingerprint all come from the proven S00 kernel - this bridge deliberately defines no proof state of its
    own, so there is exactly one taxonomy across the repository.

    A node carrying a state the kernel does not recognise is rejected rather than coerced, and a missing proof
    node is simply absent instead of being invented as PROVEN.
    """
    affected = set(downstream_invalidation(graph, changed_node_ids))
    project_id = graph.project_id
    bridged: list[EvidenceNode] = []
    for node in nodes:
        if not isinstance(node.state, ProofState):
            raise ValueError(f"non-canonical proof state at node {node.id!r}: {node.state!r} is not a kernel ProofState")
        invalidated = node.subject_fingerprint in affected or node.id in affected
        bridged.append(
            EvidenceNode(
                id=node.id,
                project_id=node.project_id,
                subject_fingerprint=node.subject_fingerprint,
                dimension=node.dimension,
                state=ProofState.INVALIDATED if invalidated else ProofState.CARRY_FORWARD,
                producer_ref=node.producer_ref,
                dependency_refs=node.dependency_refs,
                evidence_ref=None if invalidated else node.evidence_ref,
                dependency_fingerprints=node.dependency_fingerprints,
            )
        )
    return EvidenceGraph(project_id=project_id, nodes=tuple(bridged))


# CODEX-TASK[S01-PROOF-INVALIDATION-BRIDGE]
# DONE: consumes kernel ProofState/EvidenceNode/EvidenceGraph instead of declaring a competing proof state.
#       Invalidation is limited to the causal cone computed by downstream_invalidation, so unrelated siblings
#       carry forward; a node whose fingerprint is not in the graph is never invented as PROVEN.
