from __future__ import annotations
from .contracts import JobCheckpoint,LeaseState,ProductionJob,WorkerLease

def validate_lease(job:ProductionJob,lease:WorkerLease,*,now_epoch:int)->None:
    if lease.job_ref!=job.id: raise ValueError("worker lease job mismatch")
    if lease.state is not LeaseState.ACTIVE: raise ValueError("worker lease is not active")
    if lease.expires_at_epoch<=now_epoch: raise TimeoutError("worker lease expired")

def resume_sequence(job:ProductionJob,checkpoint:JobCheckpoint|None)->int:
    if checkpoint is None: return 0
    if checkpoint.job_ref!=job.id: raise ValueError("checkpoint job mismatch")
    if checkpoint.sequence<0: raise ValueError("invalid checkpoint sequence")
    return checkpoint.sequence+1

# CODEX-TASK[M40-RECOVERY]
# Add heartbeat/lease renewal, fencing token, stale-worker rejection and idempotent receipt commit.
# Retry from last proven checkpoint; never duplicate externally visible delivery side effects.
