from __future__ import annotations
from typing import Mapping
from .contracts import CreativeIntent,DirectionPlan,LockKind

def validate_direction(intent:CreativeIntent,plan:DirectionPlan,observed_locks:Mapping[str,str])->None:
    if plan.intent_id!=intent.id: raise ValueError("direction plan intent mismatch")
    if plan.variation_budget<0: raise ValueError("variation budget cannot be negative")
    if not plan.rationale_ref: raise ValueError("creative direction requires rationale evidence")
    for lock in intent.locks:
        observed=observed_locks.get(lock.key)
        if lock.kind is LockKind.HARD and observed!=lock.expected_fingerprint:
            raise ValueError(f"hard creative lock violated: {lock.key}")

# CODEX-TASK[M31-DIRECTION-SEARCH]
# Add bounded candidate direction search with explicit variation dimensions. Creative optimization may
# explore composition/style/staging only inside unlocked dimensions and must emit rationale/evidence.
