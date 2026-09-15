from ugas.audio_narrative.canon_policy import CanonChange,CanonChangeKind,CanonDelta,apply_canon_delta
from ugas.audio_narrative.contracts import AudioScene,CanonState,MusicMaster,RightsState,SceneIntent,SoundEvent,VoiceIdentity,VoiceMaster
from ugas.audio_narrative.evidence import AudioNarrativeProof,ProofState,invalidate_dimensions
from ugas.audio_narrative.golden_slice import AudioNarrativeSlice,evaluate_audio_narrative_slice


def fixture():
    canon=CanonState("p",1,"canon:f1",{"hero.name":"Ari"})
    scene=SceneIntent("scene:1","p","canon:f1",("hero",),("arrival",),4000)
    ident=VoiceIdentity("voice:hero","p","voice:f1",RightsState.VERIFIED,"rights:voice")
    voice=VoiceMaster("vm","p","vf","voice:hero","scene:1",3000,("voice:hero","scene:1"))
    music=MusicMaster("mm","p","mf","scene:1",("intro","resolve"),("stem:a",),"rights:music")
    sound=AudioScene("as","p","sf","scene:1",(SoundEvent("door","foley",100,300,"sfx:door"),),4000)
    return canon,scene,ident,voice,music,sound


def test_s03_golden_slice():
    assert len(evaluate_audio_narrative_slice(AudioNarrativeSlice(*fixture())))==4


def test_contradictory_canon_change_requires_retcon():
    canon=fixture()[0]
    try:
        apply_canon_delta(canon,CanonDelta("canon:f1",(CanonChange("hero.name","Bex",CanonChangeKind.UPDATE,"rename"),)),new_fingerprint="canon:f2")
    except ValueError as exc:
        assert "RETCON" in str(exc)
    else:
        raise AssertionError("contradictory update must fail")


def test_retcon_requires_approval():
    canon=fixture()[0]
    change=CanonChange("hero.name","Bex",CanonChangeKind.RETCON,"story revision",None)
    try: apply_canon_delta(canon,CanonDelta("canon:f1",(change,)),new_fingerprint="canon:f2")
    except ValueError as exc: assert "approval" in str(exc)
    else: raise AssertionError("unapproved retcon must fail")


def test_voice_change_does_not_invalidate_unrelated_music_proof():
    proofs=(
        AudioNarrativeProof("voice","vf",frozenset({"voice_identity","prosody"}),ProofState.PROVEN,"e1"),
        AudioNarrativeProof("music","mf",frozenset({"music_structure","music_rights"}),ProofState.PROVEN,"e2"),
    )
    changed=invalidate_dimensions(proofs,frozenset({"prosody"}))
    assert changed[0].state is ProofState.INVALIDATED
    assert changed[1].state is ProofState.CARRY_FORWARD


# CODEX-TASK[S03-A2-EXPANSION]
# Add fake-port orchestration tests for missing voice rights, cue mismatch, out-of-range sound event,
# approved retcon dependency invalidation and localized utterance repair. Keep suite provider-free.
