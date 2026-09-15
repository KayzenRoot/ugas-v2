# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
"""M03 pure domain logic: capability residuals, qualification gates and deterministic route selection.

Routing is a pure function of registered capability state. No provider is consulted, and an unqualified or
insufficient candidate is rejected rather than downgraded.
"""
from __future__ import annotations

from typing import Mapping

from ugas.foundation.contracts import ModelProfile, QualificationState, ResourceEnvelope
from ugas.foundation.invariants import model_fits_hardware

from .errors import CapabilityUnavailable, PolicyBlocked, ValidationError

ROUTABLE_QUALIFICATIONS = frozenset({QualificationState.QUALIFIED, QualificationState.PROMOTED})


def assert_routable(model: ModelProfile) -> None:
    """Only qualified or promoted profiles may serve a production route."""
    if model.qualification not in ROUTABLE_QUALIFICATIONS:
        raise PolicyBlocked(f"model {model.model_key!r} is {model.qualification.value}, not routable")


def capability_residual(model: ModelProfile, minimum_capabilities: Mapping[str, float]) -> dict[str, float]:
    """Per-capability headroom of a model over the required minimums; negative means insufficient."""
    return {
        capability: float(model.capabilities.get(capability, 0.0)) - float(minimum)
        for capability, minimum in sorted(minimum_capabilities.items())
    }


def assert_capability_sufficient(model: ModelProfile, minimum_capabilities: Mapping[str, float]) -> None:
    residual = capability_residual(model, minimum_capabilities)
    short = {name: value for name, value in residual.items() if value < 0}
    if short:
        raise CapabilityUnavailable(f"model {model.model_key!r} is short on capability: {sorted(short)}")


def assert_hardware_sufficient(model: ModelProfile, hardware: ResourceEnvelope) -> None:
    if not model_fits_hardware(model, hardware):
        raise CapabilityUnavailable(
            f"model {model.model_key!r} does not fit the measured hardware envelope"
        )


def assert_routable_candidate(model: ModelProfile, minimum_capabilities: Mapping[str, float],
                              hardware: ResourceEnvelope) -> None:
    """Full gate applied before a model may be ranked."""
    assert_routable(model)
    assert_capability_sufficient(model, minimum_capabilities)
    assert_hardware_sufficient(model, hardware)


def validate_invariants(command):
    if not command.operation:
        raise ValidationError("operation is required")
    return command


# CODEX-TASK[M03-CORE]
# DONE: qualification gate, capability residual matching and hardware fit are pure and fail closed; ranking
#       itself is delegated to the shared foundation router so tie-break semantics stay in one place.
