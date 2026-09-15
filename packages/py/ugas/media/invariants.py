from __future__ import annotations

"""Pure S02 cross-modal invariants."""
from collections.abc import Iterable

from .contracts import ArtifactState, IdentityBinding, ImageCandidate, ImageMaster, MediaArtifact, RuntimeDerivative, SpatialMaster, VideoMaster


def assert_generation_allowed(identity: IdentityBinding | None) -> None:
    if identity is None:
        return
    if identity.consent_state.value != "verified" or not identity.consent_ref:
        raise ValueError("digital-human generation requires verified consent reference")


def assert_identity_continuity(artifacts: Iterable[MediaArtifact]) -> None:
    values = list(artifacts)
    bound = [artifact.identity for artifact in values if artifact.identity is not None]
    if not bound:
        return
    project_ids = {item.project_id for item in bound}
    dna = {item.asset_dna_fingerprint for item in bound}
    human_ids = {item.human_identity_id for item in bound}
    if len(project_ids) != 1 or len(dna) != 1 or len(human_ids) != 1:
        raise ValueError("cross-modal identity drift detected")
    for item in bound:
        assert_generation_allowed(item)


def promote_image(candidate: ImageCandidate) -> ImageMaster:
    if candidate.state is not ArtifactState.ACCEPTED:
        raise ValueError("only accepted image candidate may become master")
    return ImageMaster(
        id=f"master:{candidate.id}", project_id=candidate.project_id,
        fingerprint=candidate.fingerprint, state=ArtifactState.ACCEPTED,
        identity=candidate.identity, lineage=(*candidate.lineage, candidate.id),
        width=candidate.width, height=candidate.height, selected_candidate_ref=candidate.id,
    )


def assert_selective_video_repair(video: VideoMaster, *, max_fraction: float = 0.35) -> None:
    if video.frame_count <= 0:
        raise ValueError("video frame_count must be positive")
    repaired = set()
    for window in video.repaired_windows:
        repaired.update(range(window.start_frame, window.end_frame + 1))
    if len(repaired) / video.frame_count > max_fraction:
        raise ValueError("repair scope exceeds selective-repair threshold; explicit full-regeneration reason required")


def assert_runtime_derivative(master: SpatialMaster, derivative: RuntimeDerivative) -> None:
    if master.state is not ArtifactState.ACCEPTED:
        raise ValueError("runtime derivative requires accepted spatial master")
    if derivative.source_spatial_master_ref != master.id:
        raise ValueError("runtime derivative source mismatch")
    if derivative.project_id != master.project_id:
        raise ValueError("cross-project spatial derivative")
    if master.identity != derivative.identity:
        raise ValueError("runtime derivative changed identity binding")
    if master.id not in derivative.lineage:
        raise ValueError("runtime derivative must retain source master lineage")


# CODEX-TASK[S02-LOCKED-TRAIT-EVALUATOR]
# Compare evaluator-observed identity traits against IdentityBinding.locked_traits using M05 similarity port.
# Hard locked-trait failure rejects artifact; do not average it into a quality score.
