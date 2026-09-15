from __future__ import annotations
from typing import Sequence
from .contracts import ProductionJob,WorkerProfile

def rank_workers(job:ProductionJob,workers:Sequence[WorkerProfile],*,preferred_locality_refs:frozenset[str]=frozenset())->tuple[WorkerProfile,...]:
    eligible=[w for w in workers if job.required_capabilities<=w.capabilities and w.max_concurrency>0]
    return tuple(sorted(eligible,key=lambda w:(-len(w.locality_refs & preferred_locality_refs),-w.max_concurrency,w.id)))

def choose_worker(job:ProductionJob,workers:Sequence[WorkerProfile],*,preferred_locality_refs:frozenset[str]=frozenset())->WorkerProfile:
    ranked=rank_workers(job,workers,preferred_locality_refs=preferred_locality_refs)
    if not ranked: raise ValueError("no worker satisfies production job capability envelope")
    return ranked[0]

# CODEX-TASK[M40-MEASURED-SCHEDULER]
# Combine M02 hardware telemetry, M21 failure-adjusted economics and M34 critical path. Locality is a
# preference, never permission to violate capability/quality/security constraints.
