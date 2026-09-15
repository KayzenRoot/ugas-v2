from __future__ import annotations

"""Pure S03 Golden Slice: canon -> scene -> voice/music/sound."""
from dataclasses import dataclass

from .contracts import AudioScene, CanonState, MusicMaster, SceneIntent, VoiceIdentity, VoiceMaster
from .invariants import assert_audio_timeline, assert_music_rights, assert_scene_against_canon, assert_voice_binding


@dataclass(frozen=True, slots=True)
class AudioNarrativeSlice:
    canon: CanonState
    scene: SceneIntent
    voice_identity: VoiceIdentity
    voice: VoiceMaster
    music: MusicMaster
    sound: AudioScene


def evaluate_audio_narrative_slice(value: AudioNarrativeSlice) -> tuple[str, ...]:
    assert_scene_against_canon(value.scene, value.canon)
    assert_voice_binding(value.voice, value.voice_identity, value.scene)
    assert_music_rights(value.music, value.scene)
    assert_audio_timeline(value.sound, value.scene)
    return (value.canon.fingerprint, value.voice.fingerprint, value.music.fingerprint, value.sound.fingerprint)


# CODEX-TASK[S03-GOLDEN-WIRING]
# Wire M14 -> M11/M12/M13 with fake narrative/model/audio ports. Prove canon lock, voice rights/identity,
# music rights/cue structure and sound timeline alignment. No external synthesis/provider call in A2.
