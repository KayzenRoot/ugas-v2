from __future__ import annotations
from dataclasses import dataclass
from .contracts import DecisionState

@dataclass(frozen=True,slots=True)
class QualityEvidenceStep:
    step_id:str
    kind:str
    subject_ref:str
    evidence_refs:tuple[str,...]
    causal_parent_refs:tuple[str,...]=()

@dataclass(frozen=True,slots=True)
class QualityEvidenceBundle:
    project_id:str
    artifact_fingerprint:str
    decision:DecisionState
    steps:tuple[QualityEvidenceStep,...]
    carried_proof_refs:tuple[str,...]
    invalidated_proof_refs:tuple[str,...]
    commands:tuple[str,...]
    durations_ms:tuple[int,...]
    unresolved_tasks:tuple[str,...]=()

def validate_causal_chain(bundle:QualityEvidenceBundle)->None:
    ids={s.step_id for s in bundle.steps}
    for step in bundle.steps:
        if not step.evidence_refs: raise ValueError(f"quality evidence missing: {step.step_id}")
        missing=set(step.causal_parent_refs)-ids
        if missing: raise ValueError(f"missing causal parent for {step.step_id}: {sorted(missing)}")

# CODEX-TASK[S05-GEF-EVIDENCE-BRIDGE]
# Map this causal view onto canonical GEF Evidence Spec, not a parallel source of truth. Record exact
# evaluator versions, fixtures, route economics snapshot, repair scope and proof reuse metrics.
