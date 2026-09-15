from __future__ import annotations

"""Deterministic downstream invalidation for M01 proof/test economy."""
from collections import defaultdict, deque
from typing import Iterable

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


# CODEX-TASK[S01-PROOF-INVALIDATION-BRIDGE]
# WHAT: map affected node ids to proof/evidence states PROVEN->INVALIDATED while siblings remain CARRY_FORWARD.
# INPUT: graph delta + proof registry port.
# OUTPUT: deterministic invalidation record with causal changed node ids.
# INVARIANTS: no unrelated proof invalidation; repeated same delta is idempotent.
# ERRORS: missing proof record is UNKNOWN, never silently PROVEN.
# TEST: diamond dependency, sibling isolation, repeated delta.
# DONE: M01 EvidenceSink receives stable invalidation event.
