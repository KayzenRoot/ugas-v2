# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
"""M02 pure domain logic: normalized measured hardware/resource envelopes.

The governing rule is that absence of telemetry is not zero. A probe that did not report VRAM yields None plus
an explicit UNKNOWN/DEGRADED knowledge state, never a measured 0 that downstream routing would happily fit a
model into.
"""
from __future__ import annotations

from typing import Any, Mapping

from ugas.foundation.contracts import KnowledgeState, ResourceEnvelope, content_fingerprint_of

from .errors import ValidationError

MEASURABLE_FIELDS = ("gpu_name", "vram_total_mb", "vram_available_mb", "ram_total_mb")


def classify_knowledge(reported: int) -> KnowledgeState:
    """Derive the knowledge state from how many measurable fields the probe actually reported."""
    if reported == 0:
        return KnowledgeState.UNKNOWN
    if reported == len(MEASURABLE_FIELDS):
        return KnowledgeState.KNOWN
    return KnowledgeState.DEGRADED


def normalize_probe(raw: Mapping[str, Any], *, envelope_id: str, project_id: str, version: int = 1) -> ResourceEnvelope:
    """Normalize a raw probe payload into a canonical ResourceEnvelope.

    A field the probe does not report stays None. Negative measurements, an explicit knowledge state that
    contradicts the reported measurements, and an unknown knowledge value all fail closed.
    """
    if not isinstance(raw, Mapping):
        raise ValidationError("hardware probe payload must be a mapping")

    values: dict[str, Any] = {}
    reported = 0
    for field in MEASURABLE_FIELDS:
        value = raw.get(field)
        if value is None:
            values[field] = None
            continue
        reported += 1
        if isinstance(value, bool):
            raise ValidationError(f"probe field {field} must be measured, not boolean")
        if isinstance(value, int) and value < 0:
            raise ValidationError(f"probe field {field} cannot be negative: {value}")
        if field != "gpu_name" and not isinstance(value, int):
            raise ValidationError(f"probe field {field} must be an integer measurement")
        values[field] = value

    declared = raw.get("knowledge")
    if declared is None:
        knowledge = classify_knowledge(reported)
    else:
        try:
            knowledge = KnowledgeState(str(declared))
        except ValueError:
            raise ValidationError(f"unknown hardware knowledge state: {declared!r}") from None
        if knowledge is KnowledgeState.UNKNOWN and reported:
            raise ValidationError("probe declares UNKNOWN knowledge but reports measurements")
        if knowledge is KnowledgeState.KNOWN and reported != len(MEASURABLE_FIELDS):
            raise ValidationError("probe declares KNOWN knowledge without complete measurements")

    concurrency = raw.get("concurrency_limit", 1)
    if not isinstance(concurrency, int) or isinstance(concurrency, bool) or concurrency < 1:
        raise ValidationError("concurrency_limit must be an integer >= 1")

    return ResourceEnvelope(
        id=envelope_id,
        version=version,
        fingerprint=content_fingerprint_of({
            "id": envelope_id, "version": version, "knowledge": str(knowledge),
            "gpu_name": values["gpu_name"], "vram_total_mb": values["vram_total_mb"],
            "vram_available_mb": values["vram_available_mb"], "ram_total_mb": values["ram_total_mb"],
            "concurrency_limit": concurrency,
        }),
        knowledge=knowledge,
        gpu_name=values["gpu_name"],
        vram_total_mb=values["vram_total_mb"],
        vram_available_mb=values["vram_available_mb"],
        ram_total_mb=values["ram_total_mb"],
        concurrency_limit=concurrency,
    )


def assert_usable_for_planning(envelope: ResourceEnvelope) -> None:
    """A resource envelope with no measured capacity cannot be planned against."""
    if envelope.knowledge is KnowledgeState.UNKNOWN:
        raise ValidationError("cannot plan against an envelope with UNKNOWN hardware knowledge")
    if envelope.vram_total_mb is None and envelope.ram_total_mb is None:
        raise ValidationError("cannot plan against an envelope with no measured capacity")


def plan_leases(envelope: ResourceEnvelope, requested: int, *, vram_mb_per_lease: int | None = None) -> int:
    """Return how many concurrent leases the envelope can actually support.

    Bounded by the declared concurrency limit and, when a per-lease VRAM cost is given, by measured available
    VRAM. An unknown available VRAM yields at most the declared concurrency limit; it never implies headroom.
    """
    if not isinstance(requested, int) or isinstance(requested, bool) or requested < 1:
        raise ValidationError("requested lease count must be an integer >= 1")
    assert_usable_for_planning(envelope)
    capacity = envelope.concurrency_limit
    if vram_mb_per_lease is not None:
        if vram_mb_per_lease < 1:
            raise ValidationError("vram_mb_per_lease must be >= 1")
        if envelope.vram_available_mb is None:
            return 0
        capacity = min(capacity, envelope.vram_available_mb // vram_mb_per_lease)
    return max(0, min(requested, capacity))


def validate_invariants(command):
    if not command.operation:
        raise ValidationError("operation is required")
    return command


# CODEX-TASK[M02-CORE]
# DONE: probe normalization keeps absent telemetry as None with an explicit knowledge state, rejects
#       contradictory or negative measurements, and lease planning never assumes unmeasured capacity.
