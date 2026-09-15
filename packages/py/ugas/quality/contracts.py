from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum
from typing import Mapping

class GateKind(StrEnum):
    HARD="hard"; SOFT="soft"
class DecisionState(StrEnum):
    ACCEPT="accept"; REPAIR="repair"; REGENERATE="regenerate"; REJECT="reject"

@dataclass(frozen=True,slots=True)
class QualityGate:
    id:str; kind:GateKind; minimum:float; dimension:str
@dataclass(frozen=True,slots=True)
class QualityObservation:
    gate_id:str; score:float; evidence_ref:str
@dataclass(frozen=True,slots=True)
class Defect:
    id:str; dimension:str; scope_ref:str; severity:float; evidence_ref:str
@dataclass(frozen=True,slots=True)
class RepairAction:
    defect_id:str; scope_ref:str; estimated_cost:float; invalidated_dimensions:frozenset[str]
@dataclass(frozen=True,slots=True)
class RouteEconomics:
    route_id:str; generation_cost:float; expected_repair_cost:float; expected_failure_probability:float; expected_latency_ms:int
@dataclass(frozen=True,slots=True)
class QualityDecision:
    state:DecisionState; failed_hard_gates:tuple[str,...]; defects:tuple[Defect,...]; reason_codes:tuple[str,...]

# CODEX-TASK[S05-CONTRACT-EXPANSION]
# Materialize module-owned M19 CourtCase/Verdict, M20 RepairRegion/RepairPlan/RegressionResult and
# M21 RenderPlan/CostEnvelope contracts. Keep provider prices and hardware telemetry behind ports.
