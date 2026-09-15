from __future__ import annotations
from dataclasses import dataclass
from .contracts import AppearanceDerivative,AppearanceMaster,RepresentationKind

@dataclass(frozen=True,slots=True)
class AppearanceRouteObservation:
    representation:RepresentationKind; perceptual_score:float; runtime_memory_mb:int; latency_ms:int; evidence_ref:str

def choose_representation(master:AppearanceMaster,observations:tuple[AppearanceRouteObservation,...],*,quality_floor:float,max_memory_mb:int)->RepresentationKind:
    eligible=[o for o in observations if o.perceptual_score>=quality_floor and o.runtime_memory_mb<=max_memory_mb and o.evidence_ref]
    if not eligible: raise ValueError("no appearance representation satisfies quality/runtime envelope")
    return min(eligible,key=lambda o:(o.runtime_memory_mb,o.latency_ms,o.representation.value)).representation

def validate_derivative(master:AppearanceMaster,derivative:AppearanceDerivative)->None:
    if derivative.master_ref!=master.id: raise ValueError("appearance derivative lineage mismatch")
    if not derivative.quality_evidence_ref or not derivative.runtime_ref: raise ValueError("appearance derivative requires runtime and quality evidence")
    if derivative.representation is RepresentationKind.NEURAL and not master.neural_ref: raise ValueError("neural derivative requires neural master representation")

# CODEX-TASK[M36-ROUND-TRIP]
# Implement inverse-render/material decomposition and neural->analytic/PBR distillation behind M29-qualified
# adapters. Compare neural/PBR/hybrid at target camera; use expensive neural representation only when its
# measured perceptual gain survives runtime constraints. Never discard editable PBR fallback/provenance.
