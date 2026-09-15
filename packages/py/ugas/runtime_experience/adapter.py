from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol
from .contracts import RuntimeBuild,RuntimeCompilePlan,RuntimeTarget

@dataclass(frozen=True,slots=True)
class EngineCapabilities:
    adapter_id:str; supports_streaming:bool; supports_lod:bool; supports_headless_build:bool; supported_platforms:frozenset[str]

class RuntimeEngineAdapter(Protocol):
    def capabilities(self)->EngineCapabilities: ...
    def build(self,plan:RuntimeCompilePlan,target:RuntimeTarget)->RuntimeBuild: ...

def validate_adapter(cap:EngineCapabilities,target:RuntimeTarget,plan:RuntimeCompilePlan)->None:
    if target.platform not in cap.supported_platforms: raise ValueError("engine adapter does not support target platform")
    if plan.streamed_assets and not cap.supports_streaming: raise ValueError("runtime plan requires unsupported streaming")
    if plan.fallback_refs and not cap.supports_lod: raise ValueError("runtime plan requires unsupported LOD")
    if not cap.supports_headless_build: raise ValueError("UGAS production adapter must support headless build")

# CODEX-TASK[M37-ENGINE-ADAPTERS]
# Implement adapters only after M29 qualification. Start with engine-neutral manifest and one bounded
# reference adapter. Keep Godot/other engine specifics outside domain contracts and prove headless build.
