from __future__ import annotations
from dataclasses import dataclass
from .primitives import Fingerprint,ProjectId,TraceId

@dataclass(frozen=True,slots=True)
class CausalEnvelope:
    project_id:ProjectId; trace_id:TraceId; correlation_id:str; causation_id:str|None; idempotency_key:str; actor_ref:str; capability:str; occurred_at_epoch_ms:int
@dataclass(frozen=True,slots=True)
class CommandEnvelope:
    id:str; causal:CausalEnvelope; command_type:str; payload_ref:str; expected_state:Fingerprint|None
@dataclass(frozen=True,slots=True)
class EventEnvelope:
    id:str; causal:CausalEnvelope; sequence:int; event_type:str; subject_ref:str; before:Fingerprint|None; after:Fingerprint; evidence_refs:tuple[str,...]=()

def validate_event(event:EventEnvelope)->None:
    if event.sequence<0: raise ValueError("event sequence cannot be negative")
    if not event.causal.idempotency_key: raise ValueError("idempotency key required")
    if not event.causal.capability: raise ValueError("capability required")
    if not event.causal.correlation_id: raise ValueError("correlation id required")

# CODEX-TASK[KERNEL-ENVELOPE-ADAPTERS]
# Add adapters from M01 graph events, M26 dashboard events, M27 agent actions, M32 world events and M40
# job events. Preserve domain payloads while standardizing scope/causality/idempotency/trace metadata.
