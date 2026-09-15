from __future__ import annotations
from dataclasses import dataclass, replace
from enum import StrEnum

class AdapterState(StrEnum): CANDIDATE="candidate"; QUALIFIED="qualified"; SUSPENDED="suspended"; RETIRED="retired"
@dataclass(frozen=True,slots=True)
class AdapterQualification:
    id:str; adapter_ref:str; provider_ref:str; version:str; state:AdapterState; capability_refs:frozenset[str]; license_evidence_ref:str; security_evidence_ref:str; benchmark_evidence_ref:str; hardware_envelope_ref:str; compatibility_ref:str

def assert_usable(q:AdapterQualification,required_capabilities:frozenset[str],*,requested_version:str|None=None)->None:
    """Fail-closed usability gate for a version-specific qualification.

    Passing requested_version binds the check to that exact provider version: a qualification held for
    another version is rejected rather than treated as still valid after a provider upgrade.
    """
    if q.state is not AdapterState.QUALIFIED: raise PermissionError("adapter is not qualified")
    if requested_version is not None and requested_version!=q.version:
        raise PermissionError(f"adapter version mismatch: qualified {q.version!r} requested {requested_version!r}")
    missing=required_capabilities-q.capability_refs
    if missing: raise PermissionError(f"adapter lacks capabilities: {sorted(missing)}")
    required=(q.license_evidence_ref,q.security_evidence_ref,q.benchmark_evidence_ref,q.hardware_envelope_ref,q.compatibility_ref)
    if any(not x for x in required): raise ValueError("qualified adapter lacks mandatory qualification evidence")

def requalify_on_version_change(q:AdapterQualification,new_version:str)->tuple[AdapterQualification,frozenset[str]]:
    """Apply a provider/version change, returning the adapter to CANDIDATE.

    Returns the resulting qualification and the capability refs whose dependent proofs must be invalidated.
    Only this adapter's capabilities are reported, so unrelated proofs carry forward. An unchanged version is
    a no-op that invalidates nothing.
    """
    if new_version==q.version: return q,frozenset()
    return replace(q,version=new_version,state=AdapterState.CANDIDATE),q.capability_refs

# CODEX-TASK[KERNEL-ADAPTER-REGISTRY]
# Remaining: one registry bridging M29 technology promotion, M30 DCC, M37 engines and M39 extensions.
# requalify_on_version_change() now provides the version-change semantics that registry must consume; the
# registry itself and its cross-module tests are still open and must not be claimed as done.
