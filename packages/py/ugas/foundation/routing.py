from __future__ import annotations

"""Deterministic model route selection skeleton for M02/M03 boundary."""
from dataclasses import dataclass, replace
from typing import Mapping, Sequence

from .contracts import ModelProfile, QualificationState, ResourceEnvelope, RouteDecision, content_fingerprint_of
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


def build_route_decision(selected: ScoredRoute, requirements: TaskRequirements, hardware: ResourceEnvelope) -> RouteDecision:
    """Convert a chosen ScoredRoute into a canonical, self-describing RouteDecision.

    The decision carries the requirements and hardware fingerprints it was made against, so a later
    invalidation can prove whether the decision is still valid instead of re-deriving it. Reason codes are
    stable and sorted, and the decision fingerprint is derived from semantic content only, so the same
    candidates evaluated in any input order produce an identical decision.
    """
    if not model_fits_hardware(selected.model, hardware):
        raise ValueError("cannot build a route decision from a model that does not fit the hardware envelope")
    if selected.model.qualification not in {QualificationState.QUALIFIED, QualificationState.PROMOTED}:
        raise ValueError("cannot build a route decision from an unqualified model")
    reasons = tuple(sorted(set(selected.reason_codes) | {f"REQ:{requirements.fingerprint}", f"HW:{hardware.fingerprint}"}))
    # The placeholder is excluded from the content digest (content_payload drops the fingerprint field), so it
    # cannot influence the value it is replaced by. Deriving the digest from the finished contract keeps
    # assert_fingerprint() able to verify the result.
    draft = RouteDecision(
        id=f"route:{selected.model.model_key}",
        version=selected.model.version,
        fingerprint="pending",
        model_key=selected.model.model_key,
        score=selected.score,
        reason_codes=reasons,
        hardware_fingerprint=hardware.fingerprint,
        requirements_fingerprint=requirements.fingerprint,
    )
    return replace(draft, fingerprint=content_fingerprint_of(draft))


def decide_route(models: Sequence[ModelProfile], requirements: TaskRequirements, hardware: ResourceEnvelope) -> RouteDecision:
    """Rank candidates and return the canonical decision. Raises when no qualified route satisfies constraints."""
    return build_route_decision(choose_route(models, requirements, hardware), requirements, hardware)


# CODEX-TASK[S01-ROUTE-DECISION]
# DONE: build_route_decision emits a content-derived fingerprint plus requirements/hardware fingerprints and
#       stable sorted reason codes; decide_route keeps tie-break deterministic because rank_routes already
#       breaks ties on model_key then fingerprint, so input order cannot change the winner. No provider call.
