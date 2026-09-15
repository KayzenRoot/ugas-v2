from __future__ import annotations

"""M07 bounded candidate generation/selection policy."""
from dataclasses import dataclass
from typing import Mapping, Sequence

from .contracts import ArtifactState, ImageCandidate


@dataclass(frozen=True, slots=True)
class ImageEvaluation:
    candidate_id: str
    hard_gates: Mapping[str, bool]
    quality_scores: Mapping[str, float]
    evidence_ref: str


@dataclass(frozen=True, slots=True)
class CandidatePolicy:
    max_candidates: int
    score_weights: Mapping[str, float]


def select_image_candidate(candidates: Sequence[ImageCandidate], evaluations: Sequence[ImageEvaluation], policy: CandidatePolicy) -> ImageCandidate:
    if policy.max_candidates < 1:
        raise ValueError("candidate budget must be positive")
    if len(candidates) > policy.max_candidates:
        raise ValueError("candidate generation exceeded approved budget")
    by_id = {evaluation.candidate_id: evaluation for evaluation in evaluations}
    ranked: list[tuple[float, str, ImageCandidate]] = []
    for candidate in candidates:
        evaluation = by_id.get(candidate.id)
        if evaluation is None or not evaluation.evidence_ref:
            continue
        if not all(evaluation.hard_gates.values()):
            continue
        score = sum(float(evaluation.quality_scores.get(name, 0.0)) * float(weight) for name, weight in policy.score_weights.items())
        ranked.append((score, candidate.fingerprint, candidate))
    if not ranked:
        raise ValueError("no image candidate passed hard gates with evidence")
    ranked.sort(key=lambda item: (-item[0], item[1], item[2].id))
    chosen = ranked[0][2]
    if chosen.state is ArtifactState.REJECTED:
        raise ValueError("rejected candidate cannot be selected")
    return chosen


# CODEX-TASK[M07-REPAIR-VS-REGENERATE]
# Classify localized defects into repairable regions before requesting another full candidate.
# Full regeneration consumes candidate budget and requires causal reason/evidence.
