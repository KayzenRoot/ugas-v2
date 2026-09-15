from __future__ import annotations
from .contracts import DeliveryReceipt,DeliveryTarget

def assert_delivery_ready(target:DeliveryTarget,*,artifact_fingerprint:str,provenance_ref:str,proofs:dict[str,str])->None:
    if not artifact_fingerprint or not provenance_ref: raise ValueError("delivery requires artifact fingerprint and provenance")
    missing=target.required_proof_dimensions-set(proofs)
    if missing: raise ValueError(f"delivery proof missing: {sorted(missing)}")
    if any(not proofs[d] for d in target.required_proof_dimensions): raise ValueError("delivery proof reference empty")

def issue_receipt(target:DeliveryTarget,*,receipt_id:str,artifact_fingerprint:str,provenance_ref:str,proofs:dict[str,str],delivered_ref:str)->DeliveryReceipt:
    assert_delivery_ready(target,artifact_fingerprint=artifact_fingerprint,provenance_ref=provenance_ref,proofs=proofs)
    if not delivered_ref: raise ValueError("delivered reference required")
    return DeliveryReceipt(receipt_id,target.id,artifact_fingerprint,provenance_ref,tuple(proofs[d] for d in sorted(target.required_proof_dimensions)),delivered_ref)

# CODEX-TASK[M28-EXPORT-ADAPTERS]
# Add target-profile compilers/export adapters. Export must not mutate canonical master. Receipt must
# bind exact derivative fingerprint, provenance, target profile, proofs and external delivery response.
