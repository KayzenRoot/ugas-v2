# GENERATED-DEEP-PREPROGRAMMED
"""M02 orchestration: hardware probing, resource envelopes and bounded lease planning.

Probes arrive through a port, so no real hardware, driver or GPU is touched here. Everything the module reports
is either a measurement the probe supplied or an explicit UNKNOWN/DEGRADED state.
"""
from __future__ import annotations

from typing import Any, Mapping

from ugas.foundation.contracts import KnowledgeState, ResourceEnvelope

from .domain import assert_usable_for_planning, normalize_probe, plan_leases
from .errors import CapabilityUnavailable, ValidationError


class HardwareProbeService:
    """PREPROGRAMMED orchestration boundary for M02."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> ResourceEnvelope:
        """Normalize a probe payload supplied by the probe port into a canonical envelope.

        A probe that reports nothing still yields a valid envelope with UNKNOWN knowledge and null measurements;
        it does not fail and it does not fabricate zeros.
        """
        if not isinstance(request, Mapping) or {"envelope_id", "project_id"} - set(request):
            raise ValidationError("HardwareProbeService requires envelope_id and project_id")
        probe = self._ports.get("probe")
        if probe is None:
            raise CapabilityUnavailable("HardwareProbeService requires a probe port")
        raw = await probe.read()
        return normalize_probe(raw, envelope_id=str(request["envelope_id"]),
                               project_id=str(request["project_id"]))


class ResourceEnvelopeService:
    """PREPROGRAMMED orchestration boundary for M02."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> dict[str, Any]:
        """Report the canonical shape and usability of an envelope without inventing capacity."""
        if not isinstance(request, ResourceEnvelope):
            raise ValidationError("ResourceEnvelopeService requires a canonical ResourceEnvelope")
        usable = request.knowledge is not KnowledgeState.UNKNOWN
        return {
            "envelope_id": request.id,
            "knowledge": request.knowledge.value,
            "gpu_name": request.gpu_name,
            "vram_total_mb": request.vram_total_mb,
            "vram_available_mb": request.vram_available_mb,
            "ram_total_mb": request.ram_total_mb,
            "concurrency_limit": request.concurrency_limit,
            "usable_for_planning": usable,
            "measured_fields": tuple(
                name for name, value in (
                    ("gpu_name", request.gpu_name), ("vram_total_mb", request.vram_total_mb),
                    ("vram_available_mb", request.vram_available_mb), ("ram_total_mb", request.ram_total_mb),
                ) if value is not None
            ),
        }


class LeasePlanner:
    """PREPROGRAMMED orchestration boundary for M02."""

    def __init__(self, **ports: Any):
        self._ports = ports

    async def execute(self, request: Any) -> dict[str, Any]:
        """Plan a bounded number of concurrent leases from a measured envelope."""
        if not isinstance(request, Mapping) or {"envelope", "requested"} - set(request):
            raise ValidationError("LeasePlanner requires envelope and requested")
        envelope = request["envelope"]
        if not isinstance(envelope, ResourceEnvelope):
            raise ValidationError("LeasePlanner requires a canonical ResourceEnvelope")
        granted = plan_leases(envelope, int(request["requested"]),
                              vram_mb_per_lease=request.get("vram_mb_per_lease"))
        return {
            "granted": granted,
            "requested": int(request["requested"]),
            "knowledge": envelope.knowledge.value,
            "limited_by": "unknown_capacity" if granted == 0 else "envelope",
        }


# CODEX-TASK[M02-HardwareProbeService] / [M02-ResourceEnvelopeService] / [M02-LeasePlanner]
# DONE: all three implemented through ports only. assert_usable_for_planning keeps UNKNOWN envelopes out of
#       planning, and lease planning never reads an unmeasured field as headroom.
