from ugas.quality.contracts import *
from ugas.quality.court import judge
from ugas.quality.economics import failure_adjusted_cost,choose_route
from ugas.quality.golden_slice import QualityOptimizationSlice,evaluate_quality_optimization_slice


def test_hard_gate_cannot_be_averaged_away():
    gates=(QualityGate("identity",GateKind.HARD,.95,"identity"),QualityGate("beauty",GateKind.SOFT,.1,"aesthetic"))
    obs=(QualityObservation("identity",.5,"e1"),QualityObservation("beauty",1.0,"e2"))
    d=(Defect("d1","identity","face",.9,"e3"),)
    result=judge(gates,obs,d)
    assert result.state is DecisionState.REPAIR
    assert result.failed_hard_gates==("identity",)


def test_failure_adjusted_cost_can_reverse_naive_cheapest_route():
    cheap=RouteEconomics("cheap",1.0,1.0,.7,1000)
    reliable=RouteEconomics("reliable",2.0,.2,.05,1200)
    assert failure_adjusted_cost(cheap)>failure_adjusted_cost(reliable)
    assert choose_route((cheap,reliable),max_cost=10,max_latency_ms=2000).route_id=="reliable"


def test_local_defect_invalidates_only_its_dimension():
    v=QualityOptimizationSlice(
        (QualityGate("temporal",GateKind.HARD,.9,"temporal"),),
        (QualityObservation("temporal",.5,"e1"),),
        (Defect("d1","temporal","frames:10-20",.7,"e2"),),
        {"temporal":.3},
        (RouteEconomics("repair-a",.2,.1,.05,500),),1.0,1000)
    r=evaluate_quality_optimization_slice(v)
    assert r.invalidated==frozenset({"temporal"})
    assert r.selected_route=="repair-a"


def test_missing_hard_gate_evidence_fails_closed():
    result=judge((QualityGate("rights",GateKind.HARD,1.0,"rights"),),(),())
    assert result.state is DecisionState.REJECT
    assert result.failed_hard_gates==("rights",)

# CODEX-TASK[S05-A2-EXPANSION]
# Add failed-local-repair -> regeneration escalation, seam regression, quality-floor route exclusion,
# proof reuse ratio and measured-vs-predicted economics fixtures. Keep A2 deterministic/provider-free.
