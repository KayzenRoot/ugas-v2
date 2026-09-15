from __future__ import annotations

"""Deterministic model route selection skeleton for M02/M03 boundary."""
from dataclasses import dataclass
from typing import Mapping, Sequence

from .contracts import ModelProfile, ResourceEnvelope
from .invariants import model_fits_hardware


@dataclass(frozen=True, slots=True)
class TaskRequirements:
    fingerprint: str
    capability_weights: Mapping[str, float]
    minimum_capabilities: Mapping[str, float]


@dataclass(frozen=True, slots=True)
class ScoredRoute:
    model: ModelProfile
    score: float
    reason_codes: tuple[str, ...]


def score_model(model: ModelProfile, requirements: TaskRequirements, hardware: ResourceEnvelope) -> ScoredRoute | None:
    if not model_fits_hardware(model, hardware):
        return None
    reasons: list[str] = ["QUALIFIED", "HARDWARE_FIT"]
    for capability, minimum in sorted(requirements.minimum_capabilities.items()):
        actual = float(model.capabilities.get(capability, 0.0))
        if actual < minimum:
            return None
    score = 0.0
    for capability, weight in sorted(requirements.capability_weights.items()):
        actual = float(model.capabilities.get(capability, 0.0))
        score += actual * float(weight)
        reasons.append(f"CAP:{capability}")
    return ScoredRoute(model=model, score=score, reason_codes=tuple(reasons))


def rank_routes(models: Sequence[ModelProfile], requirements: TaskRequirements, hardware: ResourceEnvelope) -> tuple[ScoredRoute, ...]:
    candidates = [route for model in models if (route := score_model(model, requirements, hardware)) is not None]
    return tuple(sorted(candidates, key=lambda route: (-route.score, route.model.model_key, route.model.fingerprint)))


def choose_route(models: Sequence[ModelProfile], requirements: TaskRequirements, hardware: ResourceEnvelope) -> ScoredRoute:
    ranked = rank_routes(models, requirements, hardware)
    if not ranked:
        raise ValueError("no qualified model route satisfies capability and hardware constraints")
    return ranked[0]


# CODEX-TASK[S01-ROUTE-DECISION]
# WHAT: convert ScoredRoute into canonical RouteDecision and persist explanation through M03 port.
# INPUT: chosen ScoredRoute + TaskRequirements + ResourceEnvelope.
# OUTPUT: deterministic RouteDecision fingerprint and reason codes.
# INVARIANTS: tie-break remains deterministic; no provider call; unqualified routes impossible.
# ERRORS: empty route set is typed NoQualifiedRoute in M03 errors.
# TEST: same candidates in different input order choose identical model and decision fingerprint.
# DONE: focused routing tests pass.
