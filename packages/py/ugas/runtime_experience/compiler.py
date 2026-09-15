from __future__ import annotations
from typing import Sequence
from .contracts import RuntimeAsset,RuntimeCompilePlan,RuntimeScene,RuntimeTarget

def compile_runtime_plan(scene:RuntimeScene,target:RuntimeTarget,assets:Sequence[RuntimeAsset])->RuntimeCompilePlan:
    by_id={a.id:a for a in assets}
    missing=set(scene.asset_refs)-set(by_id)
    if missing: raise ValueError(f"runtime assets missing: {sorted(missing)}")
    if target.budget.target_fps<=0 or target.budget.memory_mb<=0: raise ValueError("invalid runtime budget")
    resident=[]; streamed=[]; used=0
    for asset_id in scene.asset_refs:
        asset=by_id[asset_id]
        if not asset.quality_evidence_ref: raise ValueError(f"runtime asset lacks quality evidence: {asset_id}")
        if used+asset.estimated_memory_mb<=target.budget.memory_mb:
            resident.append(asset_id); used+=asset.estimated_memory_mb
        else:
            if not asset.lod_refs: raise ValueError(f"asset exceeds residency budget without LOD fallback: {asset_id}")
            streamed.append(asset_id)
    return RuntimeCompilePlan(f"plan:{scene.id}:{target.id}",scene.id,target.id,tuple(resident),tuple(streamed),tuple(by_id[a].lod_refs[-1] for a in streamed))

# CODEX-TASK[M37-PERCEPTUAL-STREAMING]
# Replace simple residency packing with camera/importance-aware cells, measured GPU/CPU/IO costs and M34
# optimizer. Preserve M10/M36 quality floors while degrading representation before semantic identity.
