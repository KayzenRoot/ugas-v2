from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum

class CommandState(StrEnum):
    REQUESTED="requested"; AUTHORIZED="authorized"; EXECUTED="executed"; REJECTED="rejected"

@dataclass(frozen=True,slots=True)
class ProjectionEvent:
    sequence:int; project_id:str; kind:str; subject_ref:str; payload_ref:str
@dataclass(frozen=True,slots=True)
class DashboardProjection:
    project_id:str; last_sequence:int; state_fingerprint:str; diagnostic_refs:tuple[str,...]=()
@dataclass(frozen=True,slots=True)
class ControlCommand:
    id:str; project_id:str; principal_id:str; capability:str; target_ref:str; state:CommandState
@dataclass(frozen=True,slots=True)
class AgentBudget:
    max_steps:int; max_tool_calls:int; max_cost:float; allowed_capabilities:frozenset[str]
@dataclass(frozen=True,slots=True)
class AgentTask:
    id:str; project_id:str; goal_ref:str; budget:AgentBudget; required_evidence:tuple[str,...]
@dataclass(frozen=True,slots=True)
class DeliveryTarget:
    id:str; project_id:str; profile:str; destination_ref:str; required_proof_dimensions:frozenset[str]
@dataclass(frozen=True,slots=True)
class DeliveryReceipt:
    id:str; target_id:str; artifact_fingerprint:str; provenance_ref:str; evidence_refs:tuple[str,...]; delivered_ref:str

# CODEX-TASK[S07-CONTRACT-EXPANSION]
# Materialize M26 realtime projection/control contracts, M27 bounded-agent execution records and M28
# export/profile/receipt contracts. Dashboard state is a projection, never canonical production truth.
