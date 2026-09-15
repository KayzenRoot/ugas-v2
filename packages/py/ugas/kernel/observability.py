from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping
from .primitives import ErrorKind

@dataclass(frozen=True,slots=True)
class FailureRecord:
    id:str; project_id:str; trace_id:str; operation_ref:str; kind:ErrorKind; retryable:bool; reason_code:str; evidence_ref:str; secret_free:bool=True
@dataclass(frozen=True,slots=True)
class OperationTelemetry:
    project_id:str; trace_id:str; operation_ref:str; duration_ms:int; cpu_ms:float; gpu_ms:float; peak_ram_mb:int; peak_vram_mb:int; cost:float; evidence_ref:str

NON_RETRYABLE_KINDS=frozenset({ErrorKind.POLICY_REJECTION,ErrorKind.QUALITY_REJECTION,ErrorKind.CAPABILITY_DENIED,ErrorKind.INTEGRITY_FAILURE})
RETRYABLE_KINDS=frozenset(ErrorKind)-NON_RETRYABLE_KINDS

SECRET_KEY_HINTS=("secret","token","password","passwd","credential","api_key","apikey","private_key","authorization","auth_header","bearer","session_key")
REDACTED="***REDACTED***"

def is_retryable(kind:ErrorKind)->bool:
    """Canonical retry classification.

    Policy, quality, capability and integrity rejections are never retryable: retrying them cannot change the
    outcome and would bypass a hard gate. Provider and transient failures are retryable, and resource
    exhaustion is retryable because capacity can return.
    """
    return kind not in NON_RETRYABLE_KINDS

def _is_secret_key(key:object)->bool:
    return any(h in str(key).lower() for h in SECRET_KEY_HINTS)

def secret_like_keys(payload:Mapping[str,object])->tuple[str,...]:
    """Payload keys that look like secret carriers, deterministically ordered."""
    return tuple(sorted(str(k) for k in payload.keys() if _is_secret_key(k)))

def assert_secret_free(payload:Mapping[str,object])->None:
    """Boundary check for records that may reach telemetry.

    Scope, stated precisely: this enforces the key-name boundary on an already-structured record. It is not a
    content scanner and does not prove that free-text values are secret-free, so callers must keep raw sensitive
    payloads out of telemetry by construction.
    """
    offenders=secret_like_keys(payload)
    if offenders: raise ValueError(f"secret-like keys must not reach telemetry: {list(offenders)}")

def redact_secrets(payload:Mapping[str,object])->dict[str,object]:
    """Copy a payload with secret-like values masked, for safe logging."""
    return {str(k):(REDACTED if _is_secret_key(k) else v) for k,v in payload.items()}

def validate_failure(record:FailureRecord)->None:
    if not record.secret_free: raise ValueError("failure record must not contain secrets")
    if not record.trace_id or not record.reason_code or not record.evidence_ref: raise ValueError("failure record lacks trace/reason/evidence")
    if record.kind in NON_RETRYABLE_KINDS and record.retryable: raise ValueError("non-retryable failure kind marked retryable")

def validate_telemetry(record:OperationTelemetry)->None:
    """Telemetry must stay trace/evidence correlated and non-negative. UNKNOWN never becomes zero."""
    if not record.trace_id or not record.operation_ref or not record.evidence_ref: raise ValueError("telemetry lacks trace/operation/evidence correlation")
    if record.duration_ms<0 or record.cpu_ms<0 or record.gpu_ms<0 or record.peak_ram_mb<0 or record.peak_vram_mb<0 or record.cost<0: raise ValueError("telemetry metrics cannot be negative")

# CODEX-TASK[KERNEL-OTEL-BRIDGE]
# Remaining: emit OpenTelemetry-compatible traces/metrics behind an adapter, consuming validate_telemetry()
# and assert_secret_free() at the boundary. The exporter adapter itself is still open.
