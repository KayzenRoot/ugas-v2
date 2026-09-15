from __future__ import annotations

"""M08 minimal temporal repair planning."""
from dataclasses import dataclass
from enum import StrEnum
from typing import Sequence

from .contracts import FrameWindow, VideoMaster


class TemporalDefectKind(StrEnum):
    IDENTITY_DRIFT = "identity_drift"
    FLICKER = "flicker"
    MOTION_DISCONTINUITY = "motion_discontinuity"
    GEOMETRY_DRIFT = "geometry_drift"
    EXPOSURE_SHIFT = "exposure_shift"


@dataclass(frozen=True, slots=True)
class TemporalDefect:
    kind: TemporalDefectKind
    window: FrameWindow
    severity: float
    evidence_ref: str


@dataclass(frozen=True, slots=True)
class TemporalRepairPlan:
    windows: tuple[FrameWindow, ...]
    full_regeneration_required: bool
    reason_codes: tuple[str, ...]


def _merge_windows(windows: Sequence[FrameWindow]) -> tuple[FrameWindow, ...]:
    ordered = sorted(windows, key=lambda w: (w.start_frame, w.end_frame))
    merged: list[FrameWindow] = []
    for window in ordered:
        if not merged or window.start_frame > merged[-1].end_frame + 1:
            merged.append(window)
        else:
            merged[-1] = FrameWindow(merged[-1].start_frame, max(merged[-1].end_frame, window.end_frame))
    return tuple(merged)


def plan_temporal_repair(video: VideoMaster, defects: Sequence[TemporalDefect], *, max_selective_fraction: float = 0.35) -> TemporalRepairPlan:
    if video.frame_count <= 0:
        raise ValueError("video frame_count must be positive")
    if any(not defect.evidence_ref for defect in defects):
        raise ValueError("every temporal defect requires evidence")
    merged = _merge_windows([defect.window for defect in defects])
    affected = sum(window.end_frame - window.start_frame + 1 for window in merged)
    fraction = affected / video.frame_count
    if fraction > max_selective_fraction:
        return TemporalRepairPlan(merged, True, (f"SELECTIVE_SCOPE_EXCEEDED:{fraction:.4f}",))
    return TemporalRepairPlan(merged, False, ("SELECTIVE_TEMPORAL_REPAIR",))


# CODEX-TASK[M08-FRAME-REPAIR-ADAPTER]
# Execute only planned windows through qualified frame/video repair port, preserve unaffected frames,
# invalidate only intersecting temporal proofs, then re-evaluate repaired windows plus seam boundaries.
