from __future__ import annotations

"""Perceptual LOD policy for target-camera compiled 3D derivatives."""
from dataclasses import dataclass
from enum import StrEnum
from typing import Sequence


class Representation(StrEnum):
    MASTER = "master"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    IMPOSTOR = "impostor"


@dataclass(frozen=True, slots=True)
class LodCandidate:
    representation: Representation
    triangle_count: int
    texture_memory_mb: int
    screen_error: float
    identity_score: float
    material_score: float
    silhouette_score: float


@dataclass(frozen=True, slots=True)
class LodPolicy:
    max_screen_error: float
    min_identity_score: float
    min_material_score: float
    min_silhouette_score: float
    max_triangles: int
    max_texture_memory_mb: int


def choose_cheapest_acceptable(candidates: Sequence[LodCandidate], policy: LodPolicy) -> LodCandidate:
    acceptable = [candidate for candidate in candidates if (
        candidate.screen_error <= policy.max_screen_error
        and candidate.identity_score >= policy.min_identity_score
        and candidate.material_score >= policy.min_material_score
        and candidate.silhouette_score >= policy.min_silhouette_score
        and candidate.triangle_count <= policy.max_triangles
        and candidate.texture_memory_mb <= policy.max_texture_memory_mb
    )]
    if not acceptable:
        raise ValueError("no LOD representation satisfies perceptual and runtime hard gates")
    return min(acceptable, key=lambda c: (c.triangle_count, c.texture_memory_mb, c.screen_error, c.representation.value))


# CODEX-TASK[M10-LOD-EVIDENCE]
# Bind each chosen LOD to renderer/evaluator evidence at target camera and preserve source master
# lineage. An impostor is allowed only when the same hard perceptual gates pass for its use case.
