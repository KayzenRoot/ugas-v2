from __future__ import annotations
from typing import Sequence
from .contracts import Defect,RepairAction

def plan_repairs(defects:Sequence[Defect],cost_by_dimension:dict[str,float])->tuple[RepairAction,...]:
    actions=[]
    for d in sorted(defects,key=lambda x:(x.scope_ref,x.dimension,x.id)):
        if not d.scope_ref or not d.evidence_ref: raise ValueError("repair requires localized defect evidence")
        if d.dimension not in cost_by_dimension: raise ValueError(f"missing repair cost model: {d.dimension}")
        actions.append(RepairAction(d.id,d.scope_ref,cost_by_dimension[d.dimension],frozenset({d.dimension})))
    return tuple(actions)

def invalidated_dimensions(actions:Sequence[RepairAction])->frozenset[str]:
    return frozenset(dim for action in actions for dim in action.invalidated_dimensions)

# CODEX-TASK[M20-REGRESSION-CHECK]
# After repair, compare repaired scope plus seam/dependency boundary. Reuse proofs outside invalidated
# dimensions. Escalate to broader regeneration only when localized repair cannot satisfy failed gates.
