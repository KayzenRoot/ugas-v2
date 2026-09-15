from __future__ import annotations

"""Hard S03 narrative/audio invariants."""
from .contracts import AudioScene, CanonState, MusicMaster, RightsState, SceneIntent, VoiceIdentity, VoiceMaster


def assert_scene_against_canon(scene: SceneIntent, canon: CanonState) -> None:
    if scene.project_id != canon.project_id:
        raise ValueError("scene/canon project mismatch")
    if scene.canon_fingerprint != canon.fingerprint:
        raise ValueError("scene references stale or different canon")
    if scene.duration_ms <= 0:
        raise ValueError("scene duration must be positive")


def assert_voice_rights(identity: VoiceIdentity) -> None:
    if identity.rights_state is not RightsState.VERIFIED or not identity.rights_ref:
        raise ValueError("voice synthesis requires verified rights/consent reference")


def assert_voice_binding(voice: VoiceMaster, identity: VoiceIdentity, scene: SceneIntent) -> None:
    assert_voice_rights(identity)
    if voice.project_id != scene.project_id or identity.project_id != scene.project_id:
        raise ValueError("voice binding crosses project boundary")
    if voice.voice_identity_ref != identity.id or voice.scene_ref != scene.id:
        raise ValueError("voice master binding mismatch")
    if identity.id not in voice.lineage or scene.id not in voice.lineage:
        raise ValueError("voice master must retain identity and scene lineage")


def assert_music_rights(music: MusicMaster, scene: SceneIntent) -> None:
    if music.project_id != scene.project_id or music.scene_ref != scene.id:
        raise ValueError("music/scene binding mismatch")
    if not music.rights_ref:
        raise ValueError("music master requires rights reference")


def assert_audio_timeline(audio: AudioScene, scene: SceneIntent) -> None:
    if audio.project_id != scene.project_id or audio.scene_ref != scene.id:
        raise ValueError("audio scene binding mismatch")
    if audio.duration_ms != scene.duration_ms:
        raise ValueError("audio scene duration must match narrative scene")
    for event in audio.events:
        if event.start_ms < 0 or event.end_ms < event.start_ms or event.end_ms > audio.duration_ms:
            raise ValueError(f"sound event outside scene timeline: {event.id}")


# CODEX-TASK[M14-CANON-DELTA]
# Implement explicit NarrativeDecision/CanonDelta. Existing canon facts cannot be silently rewritten;
# contradiction must fail or become an approved/versioned retcon with evidence and affected-proof invalidation.
