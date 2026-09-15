# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
"""M01 typed commands/results and validation boundaries."""
from dataclasses import dataclass, field
from typing import Any, Mapping

from ugas.foundation.contracts import NodeState, ProductionGraph

@dataclass(frozen=True, slots=True)
class Command:
    operation: str
    payload: Mapping[str, Any] = field(default_factory=dict)
    correlation_id: str = ""

@dataclass(frozen=True, slots=True)
class Result:
    status: str
    evidence_refs: tuple[str, ...] = ()
    data: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class TransitionRequest:
    """A single requested node state change, protected by an idempotency key."""

    project_id: str
    graph: ProductionGraph
    node_id: str
    before: NodeState
    after: NodeState
    idempotency_key: str
    request_fingerprint: str


@dataclass(frozen=True, slots=True)
class InvalidationRequest:
    project_id: str
    graph: ProductionGraph
    changed_node_ids: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class PlanningRequest:
    project_id: str
    graph: ProductionGraph
