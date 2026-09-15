from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum

class ProofState(StrEnum):
    PROVEN="proven"; CARRY_FORWARD="carry_forward"; INVALIDATED="invalidated"; UNKNOWN="unknown"

@dataclass(frozen=True,slots=True)
class ContentProof:
    proof_id:str
    subject_fingerprint:str
    dimensions:frozenset[str]
    state:ProofState
    evidence_ref:str|None

@dataclass(frozen=True,slots=True)
class ContentEvidenceBundle:
    project_id:str
    brand_fingerprint:str
    campaign_ref:str
    variant_refs:tuple[str,...]
    proofs:tuple[ContentProof,...]
    commands:tuple[str,...]
    durations_ms:tuple[int,...]
    unresolved_tasks:tuple[str,...]=()

def invalidate_content_proofs(proofs:tuple[ContentProof,...],changed:frozenset[str])->tuple[ContentProof,...]:
    out=[]
    for p in proofs:
        if p.state in {ProofState.PROVEN,ProofState.CARRY_FORWARD}:
            state=ProofState.INVALIDATED if not p.dimensions.isdisjoint(changed) else ProofState.CARRY_FORWARD
            out.append(ContentProof(p.proof_id,p.subject_fingerprint,p.dimensions,state,p.evidence_ref))
        else: out.append(p)
    return tuple(out)

# CODEX-TASK[S04-GEF-EVIDENCE-BRIDGE]
# Map to canonical GEF evidence schema. Claim, brand, localization and channel proof dimensions must
# remain independently invalidatable so a subtitle repair does not rerun unrelated brand/claim proof.
