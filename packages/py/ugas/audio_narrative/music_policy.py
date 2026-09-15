from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass(frozen=True, slots=True)
class CuePlan:
    scene_ref: str
    required_sections: tuple[str,...]
    required_stems: frozenset[str]
    max_duration_ms: int


@dataclass(frozen=True, slots=True)
class MusicCandidate:
    id: str
    fingerprint: str
    sections: tuple[str,...]
    stems: Mapping[str,str]
    duration_ms: int
    rights_ref: str


def validate_music_candidate(candidate: MusicCandidate, plan: CuePlan) -> tuple[str,...]:
    failures=[]
    if not candidate.rights_ref:
        failures.append("RIGHTS_MISSING")
    if candidate.duration_ms > plan.max_duration_ms:
        failures.append("CUE_DURATION_OVERFLOW")
    if candidate.sections != plan.required_sections:
        failures.append("CUE_STRUCTURE_MISMATCH")
    missing=plan.required_stems-set(candidate.stems)
    failures.extend(f"STEM_MISSING:{stem}" for stem in sorted(missing))
    return tuple(failures)


def select_music_candidate(candidates: Sequence[MusicCandidate], plan: CuePlan) -> MusicCandidate:
    valid=[c for c in candidates if not validate_music_candidate(c,plan)]
    if not valid:
        raise ValueError("no music candidate satisfies cue/rights/stem hard gates")
    return min(valid,key=lambda c:(c.duration_ms,c.fingerprint,c.id))


# CODEX-TASK[M12-MUSICAL-QUALITY]
# Add evaluator evidence for musical coherence, mix and narrative fit after structural hard gates.
# Never let a high aesthetic score bypass rights, required cue structure or required stems.
