from __future__ import annotations
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any
from .primitives import ErrorKind

@dataclass(frozen=True,slots=True)
class FailureRecord:
    id:str; project_id:str; trace_id:str; operation_ref:str; kind:ErrorKind; retryable:bool; reason_code:str; evidence_ref:str; secret_free:bool=True
@dataclass(frozen=True,slots=True)
class OperationTelemetry:
    project_id:str; trace_id:str; operation_ref:str; duration_ms:int; cpu_ms:float; gpu_ms:float; peak_ram_mb:int; peak_vram_mb:int; cost:float; evidence_ref:str

RETRYABLE_KINDS=frozenset({ErrorKind.TRANSIENT_FAILURE,ErrorKind.PROVIDER_FAILURE,ErrorKind.RESOURCE_EXHAUSTED})
NON_RETRYABLE_KINDS=frozenset(ErrorKind)-RETRYABLE_KINDS

SECRET_KEY_HINTS=("secret","token","password","passwd","credential","api_key","apikey","private_key","authorization","auth_header","bearer","session_key")
REDACTED="***REDACTED***"

def is_retryable(kind:ErrorKind)->bool:
    """Generic retry classification, expressed as an explicit allow-list.

    Only transient, provider and resource failures are generic retry candidates. STALE_STATE is not: a stale
    state needs reconciliation, refetch or new causal state before a retry can mean anything, so blindly
    retrying it is not a generic action. Everything else fails closed - including any ErrorKind member added
    later, which becomes non-retryable by default rather than by remembering to extend a deny-list.
    """
    return kind in RETRYABLE_KINDS

def _is_secret_key(key:object)->bool:
    return any(h in str(key).lower() for h in SECRET_KEY_HINTS)

def _walk_secret_paths(node:Any,path:str,found:list[str])->None:
    if isinstance(node,Mapping):
        for k,v in node.items():
            key=str(k); child=f"{path}.{key}" if path else key
            if _is_secret_key(k): found.append(child)
            else: _walk_secret_paths(v,child,found)
    elif isinstance(node,(list,tuple)):
        for index,item in enumerate(node): _walk_secret_paths(item,f"{path}[{index}]",found)

def secret_like_paths(payload:Any)->tuple[str,...]:
    """Dotted paths of secret-like keys anywhere in the structure, deterministically ordered.

    Recursive by design: a top-level-only check lets a nested structured secret pass the boundary unnoticed.
    """
    found:list[str]=[]
    _walk_secret_paths(payload,"",found)
    return tuple(sorted(found))

def assert_secret_free(payload:Any)->None:
    """Recursive boundary check for records that may reach telemetry.

    Enforces the key-name boundary at every depth of nested mappings and common sequences. Scope, stated
    precisely: this is not a content scanner and does not prove that free-text values are secret-free, so
    callers must still keep raw sensitive payloads out of telemetry by construction.
    """
    offenders=secret_like_paths(payload)
    if offenders: raise ValueError(f"secret-like keys must not reach telemetry: {list(offenders)}")

def redact_secrets(payload:Any)->Any:
    """Recursively mask secret-like values at any depth, preserving non-secret structure and container types.

    A secret-like key's entire value is replaced, including nested containers beneath it. Mapping key types and
    sequence types are preserved, so a redacted record stays structurally comparable to its source.
    """
    if isinstance(payload,Mapping):
        return {k:(REDACTED if _is_secret_key(k) else redact_secrets(v)) for k,v in payload.items()}
    if isinstance(payload,list): return [redact_secrets(v) for v in payload]
    if isinstance(payload,tuple): return tuple(redact_secrets(v) for v in payload)
    return payload

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
