# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
from dataclasses import dataclass, field
from typing import Any, Mapping

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
