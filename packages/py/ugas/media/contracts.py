from __future__ import annotations

"""Concrete provider-independent contracts for S02 M06-M10."""
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any, Mapping


class ConsentState(StrEnum):
    VERIFIED = "verified"
    REVOKED = "revoked"
    MISSING = "missing"


class ArtifactState(StrEnum):
    CANDIDATE = "candidate"
    REJECTED = "rejected"
    ACCEPTED = "accepted"


@dataclass(frozen=True, slots=True)
class IdentityBinding:
    project_id: str
    asset_dna_fingerprint: str
    human_identity_id: str
    consent_state: ConsentState
    consent_ref: str | None
    locked_traits: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class MediaArtifact:
    id: str
    project_id: str
    fingerprint: str
    state: ArtifactState
    identity: IdentityBinding | None
    lineage: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ImageCandidate(MediaArtifact):
    width: int = 0
    height: int = 0
    candidate_index: int = 0


@dataclass(frozen=True, slots=True)
class ImageMaster(MediaArtifact):
    width: int = 0
    height: int = 0
    selected_candidate_ref: str = ""


@dataclass(frozen=True, slots=True)
class MotionClip(MediaArtifact):
    skeleton_ref: str = ""
    duration_ms: int = 0
    contact_constraints: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class FrameWindow:
    start_frame: int
    end_frame: int

    def __post_init__(self) -> None:
        if self.start_frame < 0 or self.end_frame < self.start_frame:
            raise ValueError("invalid frame window")


@dataclass(frozen=True, slots=True)
class VideoMaster(MediaArtifact):
    fps: float = 24.0
    frame_count: int = 0
    repaired_windows: tuple[FrameWindow, ...] = ()


@dataclass(frozen=True, slots=True)
class TargetCameraProfile:
    projection: str
    yaw_deg: float
    pitch_deg: float
    distance: float
    output_width: int
    output_height: int


@dataclass(frozen=True, slots=True)
class SpatialMaster(MediaArtifact):
    mesh_ref: str = ""
    topology_fingerprint: str = ""
    uv_fingerprint: str = ""
    material_fingerprint: str = ""


@dataclass(frozen=True, slots=True)
class RuntimeDerivative(MediaArtifact):
    source_spatial_master_ref: str = ""
    target_camera: TargetCameraProfile | None = None
    triangle_count: int = 0
    texture_memory_mb: int = 0


# CODEX-TASK[S02-CONTRACT-DETAIL]
# Add module-owned evaluation/plan contracts from M06-M10 deep manifests without provider SDK types.
# Preserve source master vs runtime derivative distinction and immutable identity references.
