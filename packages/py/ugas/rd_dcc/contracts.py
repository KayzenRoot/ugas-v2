from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum

class CandidateState(StrEnum):
    CANDIDATE="candidate"; BENCHMARKED="benchmarked"; PROMOTED="promoted"; REJECTED="rejected"; HOLD="hold"

@dataclass(frozen=True,slots=True)
class TechnologyCandidate:
    id:str; name:str; version:str; source_ref:str; discovered_at:str; claimed_capabilities:frozenset[str]
    license_ref:str; security_surface_ref:str; expected_vram_gb:float|None; expected_ram_gb:float|None; state:CandidateState=CandidateState.CANDIDATE
@dataclass(frozen=True,slots=True)
class BenchmarkProtocol:
    id:str; fixture_refs:tuple[str,...]; quality_dimensions:frozenset[str]; hardware_profile_ref:str; max_vram_gb:float|None; max_duration_ms:int|None
@dataclass(frozen=True,slots=True)
class BenchmarkResult:
    candidate_id:str; protocol_id:str; quality_scores:tuple[tuple[str,float],...]; peak_vram_gb:float|None; duration_ms:int; evidence_refs:tuple[str,...]
@dataclass(frozen=True,slots=True)
class DccCheckpoint:
    id:str; scene_fingerprint:str; artifact_ref:str
@dataclass(frozen=True,slots=True)
class DccTransaction:
    id:str; project_id:str; input_checkpoint:DccCheckpoint; operation_refs:tuple[str,...]; expected_output_fingerprint:str|None=None
@dataclass(frozen=True,slots=True)
class DccExecutionResult:
    transaction_id:str; success:bool; output_checkpoint:DccCheckpoint|None; evidence_refs:tuple[str,...]; error_code:str|None=None

# CODEX-TASK[S08-CONTRACT-EXPANSION]
# Bind M29 to license/security/hardware/cost qualification and M30 to semantic DccIR operations,
# deterministic checkpoints and rollback. No candidate becomes default merely because it is newer.
