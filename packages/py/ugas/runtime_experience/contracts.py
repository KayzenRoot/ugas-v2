from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True,slots=True)
class FrameBudget:
    target_fps:int; cpu_ms:float; gpu_ms:float; memory_mb:int; streaming_mb_s:float
@dataclass(frozen=True,slots=True)
class RuntimeTarget:
    id:str; platform:str; engine_adapter:str; hardware_profile_ref:str; budget:FrameBudget
@dataclass(frozen=True,slots=True)
class RuntimeAsset:
    id:str; master_fingerprint:str; derivative_ref:str; lod_refs:tuple[str,...]; estimated_memory_mb:int; quality_evidence_ref:str
@dataclass(frozen=True,slots=True)
class RuntimeScene:
    id:str; world_snapshot_ref:str; asset_refs:tuple[str,...]; interaction_graph_ref:str; camera_profile_ref:str
@dataclass(frozen=True,slots=True)
class RuntimeCompilePlan:
    id:str; scene_ref:str; target_ref:str; resident_assets:tuple[str,...]; streamed_assets:tuple[str,...]; fallback_refs:tuple[str,...]
@dataclass(frozen=True,slots=True)
class RuntimeBuild:
    id:str; plan_ref:str; artifact_ref:str; fingerprint:str; benchmark_evidence_ref:str

# CODEX-TASK[M37-CONTRACT-EXPANSION]
# Add interaction graph/state machine, streaming cells, runtime LOD policy, engine-neutral package manifest,
# engine adapter capabilities and deterministic benchmark evidence contracts.
