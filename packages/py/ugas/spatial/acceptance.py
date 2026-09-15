from __future__ import annotations

"""M10 target-camera acceptance and runtime-budget rules.

The spatial master is judged both as source geometry/material data and by what survives the
approved gameplay camera. A cheap derivative may replace an expensive representation only
when perceptual/identity/quality floors remain satisfied.
"""
from dataclasses import dataclass
from enum import StrEnum
from typing import Mapping

from ugas.media.contracts import RuntimeDerivative, SpatialMaster, TargetCameraProfile


class SpatialGate(StrEnum):
    SOURCE_GEOMETRY = "source_geometry"
    TOPOLOGY = "topology"
    UV = "uv"
    MATERIAL = "material"
    IDENTITY = "identity"
    SCREENSPACE_READABILITY = "screenspace_readability"
    SILHOUETTE = "silhouette"
    RUNTIME_BUDGET = "runtime_budget"


@dataclass(frozen=True, slots=True)
class RuntimeBudget:
    max_triangles: int
    max_texture_memory_mb: int
    max_draw_calls: int | None = None


@dataclass(frozen=True, slots=True)
class SpatialObservation:
    gate_scores: Mapping[SpatialGate, float]
    draw_calls: int | None = None


@dataclass(frozen=True, slots=True)
class SpatialAcceptancePolicy:
    hard_minimums: Mapping[SpatialGate, float]
    target_camera: TargetCameraProfile
    runtime_budget: RuntimeBudget


@dataclass(frozen=True, slots=True)
class SpatialAcceptanceDecision:
    accepted: bool
    failed_gates: tuple[SpatialGate, ...]
    reason_codes: tuple[str, ...]


def evaluate_spatial_derivative(master: SpatialMaster, derivative: RuntimeDerivative, observation: SpatialObservation, policy: SpatialAcceptancePolicy) -> SpatialAcceptanceDecision:
    reasons: list[str] = []
    failed: list[SpatialGate] = []
    if derivative.source_spatial_master_ref != master.id:
        return SpatialAcceptanceDecision(False, (SpatialGate.IDENTITY,), ("SOURCE_MASTER_MISMATCH",))
    if derivative.target_camera != policy.target_camera:
        reasons.append("TARGET_CAMERA_PROFILE_MISMATCH")
        failed.append(SpatialGate.SCREENSPACE_READABILITY)
    for gate, minimum in sorted(policy.hard_minimums.items(), key=lambda item: item[0].value):
        actual = float(observation.gate_scores.get(gate, 0.0))
        if actual < minimum:
            failed.append(gate)
            reasons.append(f"HARD_GATE:{gate.value}:{actual:.4f}<{minimum:.4f}")
    if derivative.triangle_count > policy.runtime_budget.max_triangles:
        failed.append(SpatialGate.RUNTIME_BUDGET); reasons.append("TRIANGLE_BUDGET_EXCEEDED")
    if derivative.texture_memory_mb > policy.runtime_budget.max_texture_memory_mb:
        failed.append(SpatialGate.RUNTIME_BUDGET); reasons.append("TEXTURE_MEMORY_BUDGET_EXCEEDED")
    if policy.runtime_budget.max_draw_calls is not None and observation.draw_calls is not None and observation.draw_calls > policy.runtime_budget.max_draw_calls:
        failed.append(SpatialGate.RUNTIME_BUDGET); reasons.append("DRAW_CALL_BUDGET_EXCEEDED")
    unique_failed = tuple(sorted(set(failed), key=lambda gate: gate.value))
    return SpatialAcceptanceDecision(not unique_failed, unique_failed, tuple(reasons or ["ACCEPTED_ALL_HARD_GATES"]))


# CODEX-TASK[M10-MULTIVIEW-ROUNDTRIP]
# Add source-space + target-camera round-trip fixtures. The quality court must detect when a
# source master is technically valid but loses silhouette/material/identity readability at the
# approved isometric camera. Never encode another game's assets or protected identity as fixtures.
