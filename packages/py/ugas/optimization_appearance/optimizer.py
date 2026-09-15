from __future__ import annotations
from typing import Sequence
from .contracts import OptimizationCandidate

def expected_time_to_accept(candidate:OptimizationCandidate)->float:
    if not 0 < candidate.expected_acceptance <= 1: raise ValueError("acceptance probability must be in (0,1]")
    return candidate.expected_latency_ms/candidate.expected_acceptance

def choose_candidate(candidates:Sequence[OptimizationCandidate],*,max_cost:float)->OptimizationCandidate:
    eligible=[c for c in candidates if c.expected_cost<=max_cost and not (c.proof_reuse.carried_dimensions & c.proof_reuse.invalidated_dimensions)]
    if not eligible: raise ValueError("no optimization candidate satisfies constraints")
    return min(eligible,key=lambda c:(expected_time_to_accept(c),c.expected_cost,-len(c.proof_reuse.carried_dimensions),c.id))

# CODEX-TASK[M34-CRITICAL-PATH]
# Add DAG critical-path scheduling, M02 hardware leases, M19 quality-floor eligibility and M21 measured
# failure economics. Optimize time-to-accepted-artifact, not raw generation latency or token count.
