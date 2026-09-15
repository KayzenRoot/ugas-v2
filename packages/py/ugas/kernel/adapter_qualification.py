from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum

class AdapterState(StrEnum): CANDIDATE="candidate"; QUALIFIED="qualified"; SUSPENDED="suspended"; RETIRED="retired"
@dataclass(frozen=True,slots=True)
class AdapterQualification:
    id:str; adapter_ref:str; provider_ref:str; version:str; state:AdapterState; capability_refs:frozenset[str]; license_evidence_ref:str; security_evidence_ref:str; benchmark_evidence_ref:str; hardware_envelope_ref:str; compatibility_ref:str

def assert_usable(q:AdapterQualification,required_capabilities:frozenset[str])->None:
    if q.state is not AdapterState.QUALIFIED: raise PermissionError("adapter is not qualified")
    missing=required_capabilities-q.capability_refs
    if missing: raise PermissionError(f"adapter lacks capabilities: {sorted(missing)}")
    required=(q.license_evidence_ref,q.security_evidence_ref,q.benchmark_evidence_ref,q.hardware_envelope_ref,q.compatibility_ref)
    if any(not x for x in required): raise ValueError("qualified adapter lacks mandatory qualification evidence")

# CODEX-TASK[KERNEL-ADAPTER-REGISTRY]
# Bridge M29 technology promotion, M30 DCC, M37 engines and M39 extensions into one registry. Qualification
# is version-specific; provider/version change invalidates only dependent proofs and returns to candidate.
