from __future__ import annotations
from dataclasses import dataclass
from .contracts import *
from .court import judge
from .economics import choose_route
from .repair import plan_repairs,invalidated_dimensions

@dataclass(frozen=True,slots=True)
class QualityOptimizationSlice:
    gates:tuple[QualityGate,...]
    observations:tuple[QualityObservation,...]
    defects:tuple[Defect,...]
    repair_costs:dict[str,float]
    routes:tuple[RouteEconomics,...]
    max_cost:float
    max_latency_ms:int

@dataclass(frozen=True,slots=True)
class QualityOptimizationResult:
    decision:QualityDecision
    repairs:tuple[RepairAction,...]
    invalidated:frozenset[str]
    selected_route:str|None

def evaluate_quality_optimization_slice(v:QualityOptimizationSlice)->QualityOptimizationResult:
    decision=judge(v.gates,v.observations,v.defects)
    if decision.state is DecisionState.ACCEPT:
        return QualityOptimizationResult(decision,(),frozenset(),None)
    repairs=plan_repairs(decision.defects,v.repair_costs) if decision.defects else ()
    route=choose_route(v.routes,max_cost=v.max_cost,max_latency_ms=v.max_latency_ms) if repairs and v.routes else None
    return QualityOptimizationResult(decision,repairs,invalidated_dimensions(repairs),route.route_id if route else None)

# CODEX-TASK[S05-GOLDEN-WIRING]
# Add quality-floor eligibility before route economics and explicit REGENERATE escalation after failed
# local repair. Persist causal chain verdict -> defect -> repair -> invalidation -> route -> re-verdict.
