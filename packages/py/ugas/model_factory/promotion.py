from __future__ import annotations
from typing import Mapping
from .contracts import PromotionDecision

def decide_promotion(*,model_ref:str,baseline_ref:str,candidate_scores:Mapping[str,float],baseline_scores:Mapping[str,float],required_metrics:frozenset[str],minimum_delta:Mapping[str,float],evidence_refs:tuple[str,...])->PromotionDecision:
    missing=required_metrics-set(candidate_scores) | required_metrics-set(baseline_scores)
    if missing: return PromotionDecision(model_ref,baseline_ref,False,evidence_refs,(f"missing_metrics:{','.join(sorted(missing))}",))
    failures=[]
    for metric in sorted(required_metrics):
        delta=candidate_scores[metric]-baseline_scores[metric]
        if delta<minimum_delta.get(metric,0.0): failures.append(f"metric_regression:{metric}")
    if not evidence_refs: failures.append("missing_evidence")
    return PromotionDecision(model_ref,baseline_ref,not failures,evidence_refs,tuple(failures) if failures else ("all_required_metrics_passed",))

# CODEX-TASK[M38-STATISTICAL-PROMOTION]
# Add confidence intervals/repeated seeds, evaluator calibration and hard safety/rights/quality gates.
# Aggregate score must never hide a hard-gate regression. Promotion must be reversible to baseline.
