from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum

class LeaseState(StrEnum): OFFERED="offered"; ACTIVE="active"; EXPIRED="expired"; RELEASED="released"
@dataclass(frozen=True,slots=True)
class WorkerProfile:
    id:str; hardware_profile_ref:str; capabilities:frozenset[str]; locality_refs:frozenset[str]; max_concurrency:int
@dataclass(frozen=True,slots=True)
class ProductionJob:
    id:str; project_id:str; operation_ref:str; required_capabilities:frozenset[str]; input_fingerprints:tuple[str,...]; checkpoint_ref:str|None; idempotency_key:str
@dataclass(frozen=True,slots=True)
class WorkerLease:
    id:str; job_ref:str; worker_ref:str; state:LeaseState; expires_at_epoch:int; attempt:int
@dataclass(frozen=True,slots=True)
class JobCheckpoint:
    job_ref:str; sequence:int; state_ref:str; output_fingerprints:tuple[str,...]
@dataclass(frozen=True,slots=True)
class JobReceipt:
    job_ref:str; worker_ref:str; attempt:int; output_refs:tuple[str,...]; evidence_ref:str; success:bool

# CODEX-TASK[M40-CONTRACT-EXPANSION]
# Add queue priority, artifact locality, resumable upload/download, worker health, cancellation, retry policy,
# cost envelope and local-vs-remote route contracts. Canonical truth remains outside ephemeral workers.
