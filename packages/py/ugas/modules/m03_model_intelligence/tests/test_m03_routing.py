"""A1 focused M03 tests: qualification gates, capability residuals and deterministic routing."""
import asyncio

from ugas.foundation.contracts import (
    KnowledgeState, ModelProfile, QualificationState, ResourceEnvelope, assert_fingerprint,
)
from ugas.foundation.routing import TaskRequirements
from ugas.modules.m03_model_intelligence.domain import (
    assert_capability_sufficient, assert_routable, capability_residual,
)
from ugas.modules.m03_model_intelligence.errors import (
    CapabilityUnavailable, PolicyBlocked, ValidationError,
)
from ugas.modules.m03_model_intelligence.services_deep import (
    CapabilityMatcher, ModelRegistryService, QualificationService, RouteSelector,
)
import pytest


def run(coro):
    return asyncio.run(coro)


class FakeRegistry:
    def __init__(self, profiles=()):
        self._items = {profile.model_key: profile for profile in profiles}

    async def put(self, profile):
        self._items[profile.model_key] = profile

    async def get(self, model_key):
        return self._items.get(model_key)

    async def all(self):
        return tuple(self._items[key] for key in sorted(self._items))


def _hardware(available=7000):
    return ResourceEnvelope("hw", 1, "fh", KnowledgeState.KNOWN, "gpu", 8192, available, 24000, 1)


def _requirements():
    return TaskRequirements("rq", {"image": 1.0}, {"image": 0.7})


def _model(key, state=QualificationState.QUALIFIED, capability=0.9, min_vram=6000, fingerprint=None):
    return ModelProfile(key, 1, fingerprint or f"f-{key}", key, state, {"image": capability}, min_vram)


def test_only_qualified_or_promoted_models_are_routable():
    for state in (QualificationState.DISCOVERED, QualificationState.CANDIDATE,
                  QualificationState.REJECTED, QualificationState.SUSPENDED):
        with pytest.raises(PolicyBlocked):
            assert_routable(_model("m", state=state))
    assert_routable(_model("q"))
    assert_routable(_model("p", state=QualificationState.PROMOTED))


def test_capability_residual_reports_headroom_and_shortfall():
    model = _model("m", capability=0.8)
    assert capability_residual(model, {"image": 0.5}) == {"image": pytest.approx(0.30000000000000004)}
    assert capability_residual(model, {"image": 0.9})["image"] < 0


def test_missing_capability_counts_as_zero_not_as_present():
    model = _model("m", capability=0.9)
    assert capability_residual(model, {"audio": 0.1})["audio"] == -0.1


def test_insufficient_capability_is_rejected():
    with pytest.raises(CapabilityUnavailable):
        assert_capability_sufficient(_model("weak", capability=0.5), {"image": 0.7})


def test_selector_returns_a_sealed_canonical_decision():
    decision = run(RouteSelector().execute(
        {"requirements": _requirements(), "hardware": _hardware(), "models": [_model("model-a")]}))
    assert decision.model_key == "model-a"
    assert_fingerprint(decision)
    assert decision.hardware_fingerprint == _hardware().fingerprint


def test_selector_is_deterministic_across_input_order():
    hardware, requirements = _hardware(), _requirements()
    a, b, c = _model("model-a"), _model("model-b"), _model("model-c")
    fingerprints = {
        run(RouteSelector().execute({"requirements": requirements, "hardware": hardware, "models": order})).fingerprint
        for order in ([a, b, c], [c, b, a], [b, c, a], [c, a, b])
    }
    assert len(fingerprints) == 1, "the decision fingerprint must not depend on candidate input order"


def test_selector_skips_unqualified_candidates_and_picks_the_qualified_one():
    decision = run(RouteSelector().execute({
        "requirements": _requirements(), "hardware": _hardware(),
        "models": [_model("candidate", state=QualificationState.CANDIDATE), _model("model-a")]}))
    assert decision.model_key == "model-a"


def test_selector_fails_closed_when_nothing_qualifies():
    with pytest.raises(PolicyBlocked):
        run(RouteSelector().execute({
            "requirements": _requirements(), "hardware": _hardware(),
            "models": [_model("candidate", state=QualificationState.CANDIDATE)]}))


def test_selector_rejects_insufficient_hardware():
    with pytest.raises(PolicyBlocked):
        run(RouteSelector().execute({
            "requirements": _requirements(), "hardware": _hardware(available=1000),
            "models": [_model("big", min_vram=6000)]}))


def test_selector_can_read_from_the_registry_port():
    registry = FakeRegistry([_model("model-a")])
    decision = run(RouteSelector(registry=registry).execute(
        {"requirements": _requirements(), "hardware": _hardware()}))
    assert decision.model_key == "model-a"


def test_registry_service_seals_and_stores_a_profile():
    registry = FakeRegistry()
    stored = run(ModelRegistryService(registry=registry).execute(_model("model-a", fingerprint="pending")))
    assert stored.fingerprint != "pending"
    assert_fingerprint(stored)
    assert run(registry.get("model-a")).model_key == "model-a"


def test_registry_service_requires_a_port():
    with pytest.raises(ValidationError):
        run(ModelRegistryService().execute(_model("model-a")))


def test_matcher_reports_residual_and_sufficiency():
    report = run(CapabilityMatcher().execute(
        {"model": _model("model-a", capability=0.9), "minimum_capabilities": {"image": 0.7}}))
    assert report["sufficient"] is True
    short = run(CapabilityMatcher().execute(
        {"model": _model("model-a", capability=0.2), "minimum_capabilities": {"image": 0.7}}))
    assert short["sufficient"] is False


def test_promotion_requires_evidence():
    with pytest.raises(PolicyBlocked):
        run(QualificationService().execute({"model": _model("m"), "target_state": "promoted"}))


def test_promotion_with_evidence_succeeds_and_is_stored():
    registry = FakeRegistry([_model("m", state=QualificationState.QUALIFIED)])
    promoted = run(QualificationService(registry=registry).execute(
        {"model": _model("m"), "target_state": "promoted", "evidence_ref": "proof:m"}))
    assert promoted.qualification is QualificationState.PROMOTED
    assert run(registry.get("m")).qualification is QualificationState.PROMOTED


def test_unknown_qualification_target_is_rejected():
    with pytest.raises(ValidationError):
        run(QualificationService().execute({"model": _model("m"), "target_state": "vibes"}))
