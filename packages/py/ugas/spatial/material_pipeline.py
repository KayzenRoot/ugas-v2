from __future__ import annotations

"""M10 editable material/bake planning, designed to bridge analytic PBR and M36 appearance."""
from dataclasses import dataclass
from enum import StrEnum
from typing import Mapping


class TextureChannel(StrEnum):
    BASE_COLOR = "base_color"
    NORMAL = "normal"
    ROUGHNESS = "roughness"
    METALLIC = "metallic"
    AO = "ambient_occlusion"
    EMISSIVE = "emissive"


@dataclass(frozen=True, slots=True)
class MaterialSource:
    material_id: str
    source_fingerprint: str
    channels: frozenset[TextureChannel]
    physically_editable: bool
    rights_ref: str


@dataclass(frozen=True, slots=True)
class BakeTarget:
    resolution: int
    channels: frozenset[TextureChannel]
    max_texture_memory_mb: int


@dataclass(frozen=True, slots=True)
class MaterialPlan:
    source: MaterialSource
    target: BakeTarget
    preserve_channels: frozenset[TextureChannel]
    reconstruct_channels: frozenset[TextureChannel]


def compile_material_plan(source: MaterialSource, target: BakeTarget, required_channels: frozenset[TextureChannel]) -> MaterialPlan:
    if not source.rights_ref:
        raise ValueError("material source requires rights reference")
    if target.resolution <= 0 or target.max_texture_memory_mb <= 0:
        raise ValueError("invalid bake target budget")
    preserve = required_channels & source.channels
    reconstruct = required_channels - source.channels
    return MaterialPlan(source, target, preserve, reconstruct)


def estimate_uncompressed_rgba_mb(resolution: int, texture_count: int) -> float:
    if resolution <= 0 or texture_count < 0:
        raise ValueError("invalid texture estimate input")
    return resolution * resolution * 4 * texture_count / (1024 * 1024)


# CODEX-TASK[M10-M36-MATERIAL-ROUTE]
# Route reconstruct_channels through a qualified M36 analytic/neural appearance adapter only when
# M29 has PROMOTED it. Compare target-camera perceptual gain against memory/runtime cost. Preserve
# editable analytic/PBR fallback and source rights/provenance in every derivative.
