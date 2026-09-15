from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum

@dataclass(frozen=True,slots=True)
class ProjectId: value:str
@dataclass(frozen=True,slots=True)
class Fingerprint: value:str
@dataclass(frozen=True,slots=True)
class ArtifactRef: value:str
@dataclass(frozen=True,slots=True)
class EvidenceRef: value:str
@dataclass(frozen=True,slots=True)
class ProvenanceRef: value:str
@dataclass(frozen=True,slots=True)
class TraceId: value:str

class ErrorKind(StrEnum):
    POLICY_REJECTION="policy_rejection"
    QUALITY_REJECTION="quality_rejection"
    RESOURCE_EXHAUSTED="resource_exhausted"
    STALE_STATE="stale_state"
    CAPABILITY_DENIED="capability_denied"
    INTEGRITY_FAILURE="integrity_failure"
    PROVIDER_FAILURE="provider_failure"
    TRANSIENT_FAILURE="transient_failure"

@dataclass(frozen=True,slots=True)
class Failure:
    kind:ErrorKind; code:str; retryable:bool; evidence_ref:EvidenceRef|None=None

@dataclass(frozen=True,slots=True)
class ResourceBudget:
    max_steps:int|None=None; max_tool_calls:int|None=None; max_cost:float|None=None; max_time_ms:int|None=None; max_memory_mb:int|None=None; max_vram_mb:int|None=None

# CODEX-TASK[KERNEL-PRIMITIVE-MIGRATION]
# Migrate module-local string references incrementally. Do not perform a repo-wide blind rewrite.
# Preserve serialized compatibility through explicit adapters/versioned schemas during transition.
