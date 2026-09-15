from __future__ import annotations
from typing import Sequence
from .contracts import *

def judge(gates:Sequence[QualityGate],observations:Sequence[QualityObservation],defects:Sequence[Defect])->QualityDecision:
    by_id={o.gate_id:o for o in observations}
    failed=[]
    for gate in gates:
        obs=by_id.get(gate.id)
        if gate.kind is GateKind.HARD and (obs is None or not obs.evidence_ref or obs.score<gate.minimum): failed.append(gate.id)
    ordered_defects=tuple(sorted(defects,key=lambda d:(-d.severity,d.dimension,d.id)))
    if failed:
        return QualityDecision(DecisionState.REPAIR if ordered_defects else DecisionState.REJECT,tuple(sorted(failed)),ordered_defects,("HARD_GATE_FAILURE",))
    if ordered_defects: return QualityDecision(DecisionState.REPAIR,(),ordered_defects,("LOCALIZED_DEFECTS",))
    return QualityDecision(DecisionState.ACCEPT,(),(),("ALL_REQUIRED_GATES_PASSED",))

# CODEX-TASK[M19-SOFT-SCORING]
# Add soft-gate ranking only after all hard gates pass. Missing hard evidence fails closed. Persist
# evaluator/version/fixture refs so verdict is reproducible. A weighted score can never erase hard fail.
