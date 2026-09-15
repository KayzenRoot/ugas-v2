from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True,slots=True)
class TrustEvidence:
    check_id:str
    dimension:str
    subject_ref:str
    evidence_ref:str
    passed:bool

@dataclass(frozen=True,slots=True)
class PlatformTrustEvidenceBundle:
    project_id:str
    scope_fingerprint:str
    checks:tuple[TrustEvidence,...]
    audit_refs:tuple[str,...]
    commands:tuple[str,...]
    durations_ms:tuple[int,...]
    unresolved_tasks:tuple[str,...]=()

def assert_required_checks(bundle:PlatformTrustEvidenceBundle,required:frozenset[str])->None:
    passed={c.dimension for c in bundle.checks if c.passed and c.evidence_ref}
    missing=required-passed
    if missing: raise ValueError(f"required trust evidence missing: {sorted(missing)}")

# CODEX-TASK[S06-GEF-EVIDENCE-BRIDGE]
# Bind to canonical GEF Evidence Spec and M24 audit trail. Evidence must prove project isolation,
# provenance completeness, authorization and storage integrity without ever serializing secret values.
