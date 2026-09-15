from __future__ import annotations

"""S03 evidence and selective proof invalidation for narrative/audio production."""
from dataclasses import dataclass
from enum import StrEnum


class ProofState(StrEnum):
    PROVEN="proven"
    CARRY_FORWARD="carry_forward"
    INVALIDATED="invalidated"
    UNKNOWN="unknown"


@dataclass(frozen=True, slots=True)
class AudioNarrativeProof:
    proof_id: str
    subject_fingerprint: str
    dimensions: frozenset[str]
    state: ProofState
    evidence_ref: str | None


@dataclass(frozen=True, slots=True)
class AudioNarrativeEvidenceBundle:
    project_id: str
    canon_fingerprint: str
    scene_ref: str
    proofs: tuple[AudioNarrativeProof,...]
    commands: tuple[str,...]
    durations_ms: tuple[int,...]
    unresolved_tasks: tuple[str,...]=()


def invalidate_dimensions(proofs: tuple[AudioNarrativeProof,...], changed: frozenset[str]) -> tuple[AudioNarrativeProof,...]:
    out=[]
    for proof in proofs:
        if proof.state in {ProofState.PROVEN,ProofState.CARRY_FORWARD}:
            state=ProofState.INVALIDATED if not proof.dimensions.isdisjoint(changed) else ProofState.CARRY_FORWARD
            out.append(AudioNarrativeProof(proof.proof_id,proof.subject_fingerprint,proof.dimensions,state,proof.evidence_ref))
        else:
            out.append(proof)
    return tuple(out)


# CODEX-TASK[S03-EVIDENCE-GEF-BRIDGE]
# Bind to canonical GEF Evidence Spec after reading exact schema. Do not create a competing evidence
# source of truth. Retcon/cue/voice/sync deltas invalidate only intersecting proof dimensions.
