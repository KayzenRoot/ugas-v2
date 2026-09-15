from __future__ import annotations
from dataclasses import dataclass
from .primitives import ErrorKind

@dataclass(frozen=True,slots=True)
class FailureRecord:
    id:str; project_id:str; trace_id:str; operation_ref:str; kind:ErrorKind; retryable:bool; reason_code:str; evidence_ref:str; secret_free:bool=True
@dataclass(frozen=True,slots=True)
class OperationTelemetry:
    project_id:str; trace_id:str; operation_ref:str; duration_ms:int; cpu_ms:float; gpu_ms:float; peak_ram_mb:int; peak_vram_mb:int; cost:float; evidence_ref:str

def validate_failure(record:FailureRecord)->None:
    if not record.secret_free: raise ValueError("failure record must not contain secrets")
    if not record.trace_id or not record.reason_code or not record.evidence_ref: raise ValueError("failure record lacks trace/reason/evidence")
    non_retryable={ErrorKind.POLICY_REJECTION,ErrorKind.QUALITY_REJECTION,ErrorKind.CAPABILITY_DENIED,ErrorKind.INTEGRITY_FAILURE}
    if record.kind in non_retryable and record.retryable: raise ValueError("non-retryable failure kind marked retryable")

# CODEX-TASK[KERNEL-OTEL-BRIDGE]
# Emit OpenTelemetry-compatible traces/metrics behind an adapter. Correlate operation, evidence, cost,
# hardware and failure without logging secrets or raw sensitive payloads. Retry policy consumes ErrorKind.
