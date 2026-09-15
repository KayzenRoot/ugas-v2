from __future__ import annotations

"""Pure cross-modal S02 acceptance slice, with no provider/GPU execution."""
from dataclasses import dataclass

from .contracts import ImageMaster, MotionClip, RuntimeDerivative, SpatialMaster, VideoMaster
from .invariants import assert_identity_continuity, assert_runtime_derivative, assert_selective_video_repair


@dataclass(frozen=True, slots=True)
class CoreMediaSlice:
    image: ImageMaster
    motion: MotionClip
    video: VideoMaster
    spatial: SpatialMaster
    runtime: RuntimeDerivative


def evaluate_core_media_slice(value: CoreMediaSlice) -> tuple[str, ...]:
    artifacts = (value.image, value.motion, value.video, value.spatial, value.runtime)
    projects = {artifact.project_id for artifact in artifacts}
    if len(projects) != 1:
        raise ValueError("core media slice cannot cross projects")
    assert_identity_continuity(artifacts)
    assert_selective_video_repair(value.video)
    assert_runtime_derivative(value.spatial, value.runtime)
    if value.image.id not in value.video.lineage:
        raise ValueError("video must trace to image/identity visual source in this golden slice")
    if value.motion.id not in value.video.lineage:
        raise ValueError("video must trace to motion source in this golden slice")
    return tuple(artifact.fingerprint for artifact in artifacts)


# CODEX-TASK[S02-GOLDEN-WIRING]
# Wire M06/M07/M09/M08/M10 services with fake provider/evaluator/DCC ports around this slice.
# Test one accepted identity path plus consent failure, identity drift, oversized repair and derivative-source mismatch.
# No real GPU/model download belongs in this A2 proof.
