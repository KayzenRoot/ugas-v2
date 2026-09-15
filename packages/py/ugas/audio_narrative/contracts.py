from __future__ import annotations

"""Provider-independent contracts for S03 M11-M14."""
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Mapping


class RightsState(StrEnum):
    VERIFIED = "verified"
    MISSING = "missing"
    REVOKED = "revoked"


@dataclass(frozen=True, slots=True)
class CanonState:
    project_id: str
    version: int
    fingerprint: str
    facts: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class SceneIntent:
    id: str
    project_id: str
    canon_fingerprint: str
    character_ids: tuple[str, ...]
    beats: tuple[str, ...]
    duration_ms: int


@dataclass(frozen=True, slots=True)
class VoiceIdentity:
    id: str
    project_id: str
    identity_fingerprint: str
    rights_state: RightsState
    rights_ref: str | None


@dataclass(frozen=True, slots=True)
class VoiceMaster:
    id: str
    project_id: str
    fingerprint: str
    voice_identity_ref: str
    scene_ref: str
    duration_ms: int
    lineage: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class MusicMaster:
    id: str
    project_id: str
    fingerprint: str
    scene_ref: str
    cue_structure: tuple[str, ...]
    stem_refs: tuple[str, ...]
    rights_ref: str


@dataclass(frozen=True, slots=True)
class SoundEvent:
    id: str
    event_type: str
    start_ms: int
    end_ms: int
    asset_ref: str


@dataclass(frozen=True, slots=True)
class AudioScene:
    id: str
    project_id: str
    fingerprint: str
    scene_ref: str
    events: tuple[SoundEvent, ...]
    duration_ms: int


# CODEX-TASK[S03-CONTRACT-EXPANSION]
# Materialize module-owned utterance/prosody, cue, ambience/foley and narrative-decision contracts
# from M11-M14 deep specs. Keep rights, canon and lineage explicit and provider independent.
