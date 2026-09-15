from __future__ import annotations
from .contracts import *

def qualify(candidate:TechnologyCandidate,result:BenchmarkResult,protocol:BenchmarkProtocol,*,minimum_quality:dict[str,float])->CandidateState:
    if result.candidate_id!=candidate.id or result.protocol_id!=protocol.id: raise ValueError("benchmark identity mismatch")
    if not candidate.source_ref or not candidate.license_ref or not candidate.security_surface_ref: return CandidateState.HOLD
    if not result.evidence_refs: return CandidateState.HOLD
    scores=dict(result.quality_scores)
    if any(scores.get(dim,-1)<floor for dim,floor in minimum_quality.items()): return CandidateState.REJECTED
    if protocol.max_vram_gb is not None and (result.peak_vram_gb is None or result.peak_vram_gb>protocol.max_vram_gb): return CandidateState.HOLD
    if protocol.max_duration_ms is not None and result.duration_ms>protocol.max_duration_ms: return CandidateState.HOLD
    return CandidateState.PROMOTED

# CODEX-TASK[M29-QUALIFICATION-LEDGER]
# Persist immutable candidate/result/promotion decisions with source date, license obligations, security
# notes, measured hardware envelope and failure-adjusted economics. Requalification required on version change.
