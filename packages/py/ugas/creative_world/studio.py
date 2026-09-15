from __future__ import annotations
from typing import Sequence
from .contracts import StageState,TakePlan,TakeResult

def validate_take_plan(stage:StageState,plan:TakePlan)->None:
    if plan.stage_ref!=stage.id: raise ValueError("take stage mismatch")
    if plan.camera_ref not in stage.camera_refs: raise ValueError("camera not present on stage")
    if not plan.coverage_role: raise ValueError("coverage role required")

def select_accepted_takes(plans:Sequence[TakePlan],results:Sequence[TakeResult])->tuple[TakeResult,...]:
    by_plan={p.id:p for p in plans}; selected=[]
    for result in results:
        if result.plan_ref not in by_plan: raise ValueError("take result without plan")
        if result.accepted:
            if not result.artifact_ref or not result.quality_evidence_ref: raise ValueError("accepted take requires artifact and quality evidence")
            selected.append(result)
    return tuple(sorted(selected,key=lambda r:(by_plan[r.plan_ref].coverage_role,r.id)))

# CODEX-TASK[M33-SELECTIVE-RESHOOT]
# Add edit/coverage graph and defect-localized reshoot planner. A failed insert/angle should reshoot the
# smallest causally affected take set, preserving accepted coverage and its proofs whenever possible.
