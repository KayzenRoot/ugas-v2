from __future__ import annotations

"""S02 evidence bundle contract for cross-modal acceptance and proof reuse."""
from dataclasses import dataclass
from enum import StrEnum


class ProofState(StrEnum):
    PROVEN = "proven"
    CARRY_FORWARD = "carry_forward"
    INVALIDATED = "invalidated"
    UNKNOWN = "unknown"
    NOT_REQUIRED = "not_required"


@dataclass(frozen=True, slots=True)
class ProofRecord:
    proof_id: str
    subject_fingerprint: str
    state: ProofState
    evidence_ref: str | None
    dimensions: frozenset[str]
    causal_refs: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class MediaEvidenceBundle:
    project_id: str
    identity_fingerprint: str | None
    artifact_fingerprints: tuple[str, ...]
    proofs: tuple[ProofRecord, ...]
    commands: tuple[str, ...]
    durations_ms: tuple[int, ...]
    unresolved_tasks: tuple[str, ...] = ()


def carry_forward_unaffected(proofs: tuple[ProofRecord, ...], invalidated_dimensions: frozenset[str]) -> tuple[ProofRecord, ...]:
    result: list[ProofRecord] = []
    for proof in proofs:
        if proof.state is ProofState.PROVEN and proof.dimensions.isdisjoint(invalidated_dimensions):
            result.append(ProofRecord(proof.proof_id, proof.subject_fingerprint, ProofState.CARRY_FORWARD, proof.evidence_ref, proof.dimensions, proof.causal_refs))
        elif proof.state in {ProofState.PROVEN, ProofState.CARRY_FORWARD} and not proof.dimensions.isdisjoint(invalidated_dimensions):
            result.append(ProofRecord(proof.proof_id, proof.subject_fingerprint, ProofState.INVALIDATED, proof.evidence_ref, proof.dimensions, proof.causal_refs))
        else:
            result.append(proof)
    return tuple(result)


# CODEX-TASK[S02-EVIDENCE-PERSISTENCE]
# Bind this bundle to canonical GEF Evidence Spec after checking exact schema. Do not invent a
# parallel source of truth. Record exact head/base, touched files, A0/A1/A2 commands/results,
# proof carry-forward/invalidation, durations, blockers and remaining CODEX-TASK ids.
