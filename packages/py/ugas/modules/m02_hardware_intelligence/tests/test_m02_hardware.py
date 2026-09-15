"""A1 focused M02 tests: hardware truth, UNKNOWN/DEGRADED semantics and bounded lease planning."""
import asyncio

from ugas.foundation.contracts import KnowledgeState, ResourceEnvelope
from ugas.modules.m02_hardware_intelligence.domain import (
    assert_usable_for_planning, classify_knowledge, normalize_probe, plan_leases,
)
from ugas.modules.m02_hardware_intelligence.errors import CapabilityUnavailable, ValidationError
from ugas.modules.m02_hardware_intelligence.services_deep import (
    HardwareProbeService, LeasePlanner, ResourceEnvelopeService,
)
import pytest


def run(coro):
    return asyncio.run(coro)


class FakeProbe:
    def __init__(self, payload):
        self.payload = payload

    async def read(self):
        return self.payload


FULL = {"gpu_name": "gpu-x", "vram_total_mb": 8192, "vram_available_mb": 7000, "ram_total_mb": 24000}


def test_classify_knowledge_reflects_what_was_reported():
    assert classify_knowledge(0) is KnowledgeState.UNKNOWN
    assert classify_knowledge(2) is KnowledgeState.DEGRADED
    assert classify_knowledge(4) is KnowledgeState.KNOWN


def test_absent_telemetry_is_unknown_not_zero():
    envelope = normalize_probe({}, envelope_id="hw", project_id="p")
    assert envelope.knowledge is KnowledgeState.UNKNOWN
    assert envelope.vram_available_mb is None
    assert envelope.vram_available_mb != 0, "missing telemetry must not become a measured zero"
    assert envelope.gpu_name is None, "GPU capability must not be inferred"


def test_partial_probe_is_degraded_and_keeps_measured_values():
    envelope = normalize_probe({"vram_total_mb": 8192}, envelope_id="hw", project_id="p")
    assert envelope.knowledge is KnowledgeState.DEGRADED
    assert envelope.vram_total_mb == 8192
    assert envelope.vram_available_mb is None


def test_full_probe_is_known():
    envelope = normalize_probe(FULL, envelope_id="hw", project_id="p")
    assert envelope.knowledge is KnowledgeState.KNOWN
    assert envelope.vram_available_mb == 7000


def test_negative_measurement_is_rejected():
    with pytest.raises(ValidationError):
        normalize_probe({"vram_total_mb": -1}, envelope_id="hw", project_id="p")


def test_unknown_knowledge_contradicted_by_measurements_is_rejected():
    with pytest.raises(ValidationError):
        normalize_probe({"knowledge": "unknown", "vram_total_mb": 8192}, envelope_id="hw", project_id="p")


def test_known_knowledge_without_full_measurements_is_rejected():
    with pytest.raises(ValidationError):
        normalize_probe({"knowledge": "known", "vram_total_mb": 8192}, envelope_id="hw", project_id="p")


def test_undeclared_knowledge_state_is_rejected():
    with pytest.raises(ValidationError):
        normalize_probe({"knowledge": "probably_fine"}, envelope_id="hw", project_id="p")


def test_unknown_envelope_cannot_be_planned_against():
    envelope = normalize_probe({}, envelope_id="hw", project_id="p")
    with pytest.raises(ValidationError):
        assert_usable_for_planning(envelope)
    with pytest.raises(ValidationError):
        plan_leases(envelope, 1)


def test_lease_planning_is_bounded_by_declared_concurrency():
    envelope = normalize_probe(FULL, envelope_id="hw", project_id="p")
    assert plan_leases(envelope, 3) == 1, "declared concurrency limit bounds the plan"


def test_lease_planning_is_bounded_by_measured_vram():
    envelope = normalize_probe({**FULL, "concurrency_limit": 8, "vram_available_mb": 6000},
                               envelope_id="hw", project_id="p")
    assert plan_leases(envelope, 8, vram_mb_per_lease=2000) == 3


def test_unmeasured_vram_yields_no_vram_bound_leases():
    envelope = normalize_probe({"ram_total_mb": 24000, "concurrency_limit": 4},
                               envelope_id="hw", project_id="p")
    assert plan_leases(envelope, 4, vram_mb_per_lease=2000) == 0, "unknown VRAM is not headroom"


def test_probe_service_requires_a_probe_port():
    with pytest.raises(CapabilityUnavailable):
        run(HardwareProbeService().execute({"envelope_id": "hw", "project_id": "p"}))


def test_probe_service_normalizes_through_the_port():
    envelope = run(HardwareProbeService(probe=FakeProbe(FULL)).execute({"envelope_id": "hw", "project_id": "p"}))
    assert envelope.knowledge is KnowledgeState.KNOWN and envelope.gpu_name == "gpu-x"


def test_probe_service_keeps_an_empty_probe_explicit():
    envelope = run(HardwareProbeService(probe=FakeProbe({})).execute({"envelope_id": "hw", "project_id": "p"}))
    assert envelope.knowledge is KnowledgeState.UNKNOWN


def test_envelope_service_reports_measured_fields_only():
    report = run(ResourceEnvelopeService().execute(
        normalize_probe({"vram_total_mb": 8192}, envelope_id="hw", project_id="p")))
    assert report["measured_fields"] == ("vram_total_mb",)
    assert report["usable_for_planning"] is True


def test_lease_planner_reports_unknown_capacity_limiting():
    envelope = normalize_probe(FULL, envelope_id="hw", project_id="p")
    report = run(LeasePlanner().execute({"envelope": envelope, "requested": 4}))
    assert report["granted"] == 1 and report["knowledge"] == "known"
