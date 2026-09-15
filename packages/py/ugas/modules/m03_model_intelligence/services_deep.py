# GENERATED-DEEP-PREPROGRAMMED
"""M03 orchestration: qualified model registry, capability matching and route selection.

Routing never calls a provider. Candidates are filtered by the M03 domain gates and then ranked by the shared
foundation router, so the winner and its tie-break are deterministic and independent of input order.
"""
from __future__ import annotations

from dataclasses import replace
from typing import Any, Mapping

from ugas.foundation.contracts import ModelProfile, QualificationState, ResourceEnvelope, RouteDecision, content_fingerprint_of
from ugas.foundation.routing import TaskRequirements, build_route_decision, rank_routes

from .domain import assert_routable, assert_routable_candidate, capability_residual
from .errors import CapabilityUnavailable, PolicyBlocked, ValidationError


def _resign(profile: ModelProfile) -> ModelProfile:
    return replace(profile, fingerprint=content_fingerprint_of(profile))


class ModelRegistryService:
    """PREPROGRAMMED orchestration boundary for M03."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> ModelProfile:
        """Register or replace a model profile in the registry port."""
        if not isinstance(request, ModelProfile):
            raise ValidationError("ModelRegistryService requires a canonical ModelProfile")
        registry = self._ports.get("registry")
        if registry is None:
            raise ValidationError("ModelRegistryService requires a registry port")
        sealed = _resign(request)
        await registry.put(sealed)
        return sealed


class CapabilityMatcher:
    """PREPROGRAMMED orchestration boundary for M03."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> dict[str, Any]:
        """Report per-capability residual for one model against the requested minimums."""
        if not isinstance(request, Mapping) or {"model", "minimum_capabilities"} - set(request):
            raise ValidationError("CapabilityMatcher requires model and minimum_capabilities")
        model = request["model"]
        if not isinstance(model, ModelProfile):
            raise ValidationError("CapabilityMatcher requires a canonical ModelProfile")
        residual = capability_residual(model, request["minimum_capabilities"])
        return {
            "model_key": model.model_key,
            "residual": residual,
            "sufficient": all(value >= 0 for value in residual.values()),
        }


class RouteSelector:
    """PREPROGRAMMED orchestration boundary for M03."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> RouteDecision:
        """Select a route from the registry and return a canonical RouteDecision.

        Every candidate passes the qualification, capability and hardware gates before ranking; if no candidate
        survives, the request fails closed instead of returning a degraded route.
        """
        if not isinstance(request, Mapping) or {"requirements", "hardware"} - set(request):
            raise ValidationError("RouteSelector requires requirements and hardware")
        requirements, hardware = request["requirements"], request["hardware"]
        if not isinstance(requirements, TaskRequirements) or not isinstance(hardware, ResourceEnvelope):
            raise ValidationError("RouteSelector requires canonical requirements and hardware")

        candidates = request.get("models")
        if candidates is None:
            registry = self._ports.get("registry")
            if registry is None:
                raise ValidationError("RouteSelector requires either models or a registry port")
            candidates = await registry.all()

        eligible: list[ModelProfile] = []
        for model in candidates:
            try:
                assert_routable_candidate(model, requirements.minimum_capabilities, hardware)
            except (PolicyBlocked, CapabilityUnavailable):
                # Only the two gate failures are expected here. Anything else is a real defect and must
                # propagate rather than silently shrinking the candidate set.
                continue
            eligible.append(model)
        if not eligible:
            raise PolicyBlocked("no qualified model route satisfies capability and hardware constraints")

        ranked = rank_routes(eligible, requirements, hardware)
        if not ranked:
            raise PolicyBlocked("no qualified model route satisfies capability and hardware constraints")
        return build_route_decision(ranked[0], requirements, hardware)


class QualificationService:
    """PREPROGRAMMED orchestration boundary for M03."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> ModelProfile:
        """Apply a bounded qualification transition to a registered model.

        Promotion requires an evidence reference; a promotion without evidence is a policy failure rather than a
        silent state change.
        """
        if not isinstance(request, Mapping) or {"model", "target_state"} - set(request):
            raise ValidationError("QualificationService requires model and target_state")
        model = request["model"]
        if not isinstance(model, ModelProfile):
            raise ValidationError("QualificationService requires a canonical ModelProfile")
        try:
            target = QualificationState(str(request["target_state"]))
        except ValueError:
            raise ValidationError(f"unknown qualification state: {request['target_state']!r}") from None
        if target is QualificationState.PROMOTED and not request.get("evidence_ref"):
            raise PolicyBlocked("promotion requires an evidence reference")
        promoted = _resign(replace(model, qualification=target))
        registry = self._ports.get("registry")
        if registry is not None:
            await registry.put(promoted)
        return promoted


# CODEX-TASK[M03-ModelRegistryService] / [M03-CapabilityMatcher] / [M03-RouteSelector] / [M03-QualificationService]
# DONE: all four implemented. Route selection applies the full gate then delegates ranking to the shared
#       foundation router; no provider SDK is imported and no provider call is possible.
