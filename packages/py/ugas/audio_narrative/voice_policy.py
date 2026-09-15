from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from .contracts import VoiceIdentity
from .invariants import assert_voice_rights


@dataclass(frozen=True, slots=True)
class VoiceCandidate:
    id: str
    fingerprint: str
    identity_ref: str
    duration_ms: int


@dataclass(frozen=True, slots=True)
class VoiceEvaluation:
    candidate_id: str
    identity_score: float
    prosody_score: float
    intelligibility_score: float
    hard_gates: Mapping[str, bool]
    evidence_ref: str


@dataclass(frozen=True, slots=True)
class VoicePolicy:
    max_candidates: int
    min_identity: float
    min_prosody: float
    min_intelligibility: float


def select_voice_candidate(identity: VoiceIdentity, candidates: Sequence[VoiceCandidate], evaluations: Sequence[VoiceEvaluation], policy: VoicePolicy) -> VoiceCandidate:
    assert_voice_rights(identity)
    if len(candidates) > policy.max_candidates:
        raise ValueError("voice candidate budget exceeded")
    by_id = {e.candidate_id:e for e in evaluations}
    accepted=[]
    for candidate in candidates:
        e=by_id.get(candidate.id)
        if candidate.identity_ref != identity.id or e is None or not e.evidence_ref or not all(e.hard_gates.values()):
            continue
        if e.identity_score < policy.min_identity or e.prosody_score < policy.min_prosody or e.intelligibility_score < policy.min_intelligibility:
            continue
        score=e.identity_score+e.prosody_score+e.intelligibility_score
        accepted.append((score,candidate.fingerprint,candidate))
    if not accepted:
        raise ValueError("no voice candidate passed governed acceptance")
    accepted.sort(key=lambda x:(-x[0],x[1],x[2].id))
    return accepted[0][2]


# CODEX-TASK[M11-UTTERANCE-REPAIR]
# Localize pronunciation/prosody defects to utterance spans and resynthesize only affected spans
# when identity continuity and seam quality can be preserved. Full take regeneration needs reason.
