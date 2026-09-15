from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum

class RepresentationKind(StrEnum):
    PBR="pbr"; NEURAL="neural"; HYBRID="hybrid"

@dataclass(frozen=True,slots=True)
class ProofReusePlan:
    carried_dimensions:frozenset[str]; invalidated_dimensions:frozenset[str]
@dataclass(frozen=True,slots=True)
class OptimizationCandidate:
    id:str; route_ref:str; expected_acceptance:float; expected_latency_ms:int; expected_cost:float; proof_reuse:ProofReusePlan
@dataclass(frozen=True,slots=True)
class ExperienceContext:
    id:str; project_id:str; cohort_ref:str|None; accessibility_needs:frozenset[str]; privacy_scope_ref:str
@dataclass(frozen=True,slots=True)
class ExperienceVariant:
    id:str; master_fingerprint:str; changed_dimensions:frozenset[str]; experiment_variable:str|None; reversible:bool
@dataclass(frozen=True,slots=True)
class AppearanceMaster:
    id:str; asset_fingerprint:str; representation:RepresentationKind; editable_pbr_ref:str; neural_ref:str|None; provenance_ref:str
@dataclass(frozen=True,slots=True)
class AppearanceDerivative:
    id:str; master_ref:str; target_camera_ref:str; hardware_profile_ref:str; representation:RepresentationKind; runtime_ref:str; quality_evidence_ref:str

# CODEX-TASK[S10-CONTRACT-EXPANSION]
# Materialize M34 critical-path/failure-economics contracts, M35 privacy/accessibility experiment records,
# and M36 inverse-render/neural-material/analytic-distillation contracts. Preserve editable master lineage.
