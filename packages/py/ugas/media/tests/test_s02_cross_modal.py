from ugas.media.contracts import (
    ArtifactState, ConsentState, FrameWindow, IdentityBinding, ImageMaster,
    MotionClip, RuntimeDerivative, SpatialMaster, TargetCameraProfile, VideoMaster,
)
from ugas.media.evidence import ProofRecord, ProofState, carry_forward_unaffected
from ugas.media.golden_slice import CoreMediaSlice, evaluate_core_media_slice
from ugas.media.video_repair import TemporalDefect, TemporalDefectKind, plan_temporal_repair


def identity() -> IdentityBinding:
    return IdentityBinding("p", "dna:f1", "human:1", ConsentState.VERIFIED, "consent:1", {"face":"locked"})


def artifacts():
    ident = identity()
    image = ImageMaster("img", "p", "fi", ArtifactState.ACCEPTED, ident, (), 1024,1024,"cand")
    motion = MotionClip("motion", "p", "fm", ArtifactState.ACCEPTED, ident, (), "rig", 1000, ("left_foot",))
    video = VideoMaster("vid", "p", "fv", ArtifactState.ACCEPTED, ident, ("img","motion"), 24.0, 240, ())
    spatial = SpatialMaster("spatial", "p", "fs", ArtifactState.ACCEPTED, ident, (), "mesh","topo","uv","mat")
    camera = TargetCameraProfile("perspective",45,55,12,1920,1080)
    runtime = RuntimeDerivative("runtime", "p", "fr", ArtifactState.ACCEPTED, ident, ("spatial",), "spatial", camera, 45000,220)
    return image,motion,video,spatial,runtime


def test_s02_golden_slice_accepts_consistent_identity_and_lineage():
    assert len(evaluate_core_media_slice(CoreMediaSlice(*artifacts()))) == 5


def test_temporal_repair_is_local_when_scope_is_small():
    *_, video, _, _ = ()  # placeholder kept out of provider path


def test_temporal_windows_merge_and_remain_selective():
    video = artifacts()[2]
    defects = [
        TemporalDefect(TemporalDefectKind.FLICKER, FrameWindow(10,20), .5, "e1"),
        TemporalDefect(TemporalDefectKind.MOTION_DISCONTINUITY, FrameWindow(18,30), .8, "e2"),
    ]
    plan = plan_temporal_repair(video, defects)
    assert plan.windows == (FrameWindow(10,30),)
    assert not plan.full_regeneration_required


def test_unaffected_quality_proof_is_carried_forward():
    proofs = (
        ProofRecord("identity","fi",ProofState.PROVEN,"e1",frozenset({"identity"})),
        ProofRecord("temporal","fv",ProofState.PROVEN,"e2",frozenset({"temporal"})),
    )
    updated = carry_forward_unaffected(proofs, frozenset({"temporal"}))
    assert updated[0].state is ProofState.CARRY_FORWARD
    assert updated[1].state is ProofState.INVALIDATED


# CODEX-TASK[S02-TEST-CORRECTION]
# Remove the intentionally incomplete placeholder test above while materializing S02 and replace it
# with a real oversized-window/full-regeneration assertion. Add consent failure, identity drift,
# motion contact and target-camera spatial acceptance to the same bounded A2 suite.
