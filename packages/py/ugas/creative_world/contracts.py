from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum

class LockKind(StrEnum):
    HARD="hard"; SOFT="soft"

@dataclass(frozen=True,slots=True)
class CreativeLock:
    key:str; expected_fingerprint:str; kind:LockKind
@dataclass(frozen=True,slots=True)
class CreativeIntent:
    id:str; project_id:str; objective:str; locks:tuple[CreativeLock,...]; reference_refs:tuple[str,...]=()
@dataclass(frozen=True,slots=True)
class DirectionPlan:
    id:str; intent_id:str; scene_refs:tuple[str,...]; variation_budget:int; rationale_ref:str
@dataclass(frozen=True,slots=True)
class WorldEntity:
    id:str; state_fingerprint:str
@dataclass(frozen=True,slots=True)
class WorldEvent:
    id:str; cause_refs:tuple[str,...]; target_entity_id:str; before_fingerprint:str; after_fingerprint:str
@dataclass(frozen=True,slots=True)
class WorldSnapshot:
    id:str; project_id:str; version:int; entity_states:tuple[WorldEntity,...]; parent_snapshot_ref:str|None=None
@dataclass(frozen=True,slots=True)
class StageState:
    id:str; world_snapshot_ref:str; asset_refs:tuple[str,...]; lighting_ref:str; camera_refs:tuple[str,...]
@dataclass(frozen=True,slots=True)
class TakePlan:
    id:str; stage_ref:str; camera_ref:str; performance_refs:tuple[str,...]; coverage_role:str
@dataclass(frozen=True,slots=True)
class TakeResult:
    id:str; plan_ref:str; artifact_ref:str; quality_evidence_ref:str; accepted:bool

# CODEX-TASK[S09-CONTRACT-EXPANSION]
# Materialize M31 creative kernel/constraint contracts, M32 causal world-delta contracts and M33
# stage/camera/light/performance/edit contracts. Rendered pixels never become canonical world state.
