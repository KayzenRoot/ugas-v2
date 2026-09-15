# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
"""M01 pure domain logic: graph invariants, legal transitions and deterministic execution planning.

Delegates every invariant to the shared foundation so M01 owns lifecycle semantics without re-deriving them.
"""
from __future__ import annotations

from dataclasses import replace

from ugas.foundation.contracts import GraphNode, NodeState, ProductionGraph
from ugas.foundation.invariants import assert_graph, assert_legal_transition

from .errors import StaleState, ValidationError


def apply_transition(graph: ProductionGraph, node_id: str, before: NodeState, after: NodeState) -> ProductionGraph:
    """Return the graph with one node transitioned, or fail closed.

    The declared `before` state must match the node's actual state: a caller operating on a stale view of the
    graph needs reconciliation, not a blind retry, so it is reported as a typed StaleState.
    """
    assert_graph(graph)
    match = [node for node in graph.nodes if node.id == node_id]
    if not match:
        raise ValidationError(f"unknown graph node: {node_id}")
    current = match[0].state
    if current != before:
        raise StaleState(f"node {node_id} is {current.value}, caller expected {before.value}")
    assert_legal_transition(before, after)
    updated = tuple(
        GraphNode(node.id, node.version, node.fingerprint, node.project_id, after, node.ir_ref, node.artifact_refs)
        if node.id == node_id else node
        for node in graph.nodes
    )
    return replace(graph, nodes=updated, fingerprint="pending")


def execution_plan(graph: ProductionGraph) -> tuple[str, ...]:
    """Deterministic topological order of schedulable nodes.

    Only nodes that can actually be scheduled are returned: an ACCEPTED or INVALIDATED node needs no further
    execution. Ties are broken by node id so the plan never depends on declaration order.
    """
    assert_graph(graph)
    runnable = {node.id for node in graph.nodes if node.state in {NodeState.READY, NodeState.PLANNED}}
    incoming = {node_id: 0 for node_id in runnable}
    outgoing: dict[str, list[str]] = {node_id: [] for node_id in runnable}
    for edge in graph.edges:
        if edge.source in runnable and edge.target in runnable:
            outgoing[edge.source].append(edge.target)
            incoming[edge.target] += 1
    ready = sorted(node_id for node_id, degree in incoming.items() if degree == 0)
    plan: list[str] = []
    while ready:
        current = ready.pop(0)
        plan.append(current)
        for target in sorted(outgoing[current]):
            incoming[target] -= 1
            if incoming[target] == 0:
                ready.append(target)
                ready.sort()
    return tuple(plan)


def assert_project_scope(project_id: str, graph: ProductionGraph) -> None:
    if project_id != graph.project_id:
        raise ValidationError(f"request project {project_id!r} does not own graph {graph.project_id!r}")


def validate_invariants(command):
    if not command.operation:
        raise ValidationError("operation is required")
    return command


# CODEX-TASK[M01-CORE]
# DONE: graph invariants, stale-view detection and deterministic planning live here; cyclic graphs are rejected
#       through the shared foundation assert_graph rather than a second implementation.
