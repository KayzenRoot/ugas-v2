"""A1 deterministic routing and canonical RouteDecision tests."""
from ugas.foundation.contracts import KnowledgeState, ModelProfile, QualificationState, ResourceEnvelope, assert_fingerprint
from ugas.foundation.routing import TaskRequirements, build_route_decision, choose_route, decide_route, rank_routes
import pytest


def _hardware(available=7000, knowledge=KnowledgeState.KNOWN):
    return ResourceEnvelope("hw", 1, "fh", knowledge, "gpu", 8192, available, 24000, 1)


def _requirements():
    return TaskRequirements("rq", {"image": 1.0}, {"image": 0.7})


def _model(key, state=QualificationState.QUALIFIED, capability=0.9, min_vram=6000):
    return ModelProfile(key, 1, f"f-{key}", key, state, {"image": capability}, min_vram)


def test_only_qualified_or_promoted_models_can_route():
    hardware, requirements = _hardware(), _requirements()
    for state in (QualificationState.DISCOVERED, QualificationState.CANDIDATE,
                  QualificationState.REJECTED, QualificationState.SUSPENDED):
        with pytest.raises(ValueError):
            choose_route([_model("m", state=state)], requirements, hardware)
    assert choose_route([_model("q")], requirements, hardware).model.model_key == "q"


def test_insufficient_capability_is_rejected():
    with pytest.raises(ValueError):
        choose_route([_model("weak", capability=0.5)], _requirements(), _hardware())


def test_insufficient_hardware_is_rejected():
    with pytest.raises(ValueError):
        choose_route([_model("big", min_vram=16000)], _requirements(), _hardware(available=7000))


def test_input_order_cannot_change_the_winner():
    hardware, requirements = _hardware(), _requirements()
    a, b, c = _model("model-a"), _model("model-b"), _model("model-c")
    orders = ([a, b, c], [c, b, a], [b, a, c], [b, c, a], [c, a, b], [a, c, b])
    winners = {choose_route(order, requirements, hardware).model.model_key for order in orders}
    assert winners == {"model-a"}, "tie-break must be deterministic and independent of input order"


def test_ranking_is_deterministic_and_score_ordered():
    hardware, requirements = _hardware(), _requirements()
    better = _model("better", capability=0.95)
    worse = _model("worse", capability=0.8)
    ranked = rank_routes([worse, better], requirements, hardware)
    assert [route.model.model_key for route in ranked] == ["better", "worse"]
    assert ranked == rank_routes([better, worse], requirements, hardware)


def test_unknown_hardware_does_not_grant_capability():
    """Absent telemetry must not be read as sufficient capacity."""
    unknown = ResourceEnvelope("hw", 1, "fh", KnowledgeState.UNKNOWN, None, None, None, None)
    assert unknown.vram_available_mb is None, "missing telemetry is not zero"
    with pytest.raises(ValueError):
        choose_route([_model("needs-vram", min_vram=6000)], _requirements(), unknown)


def test_route_decision_is_deterministic_and_self_describing():
    hardware, requirements = _hardware(), _requirements()
    first = decide_route([_model("model-a")], requirements, hardware)
    second = decide_route([_model("model-a")], requirements, hardware)
    assert first.fingerprint == second.fingerprint
    assert first.hardware_fingerprint == hardware.fingerprint
    assert first.requirements_fingerprint == requirements.fingerprint
    assert_fingerprint(first)


def test_decision_fingerprint_carries_every_semantic_field():
    hardware, requirements = _hardware(), _requirements()
    base = decide_route([_model("model-a")], requirements, hardware)
    assert base.fingerprint != decide_route([_model("model-b")], requirements, hardware).fingerprint
    other_requirements = TaskRequirements("rq-2", {"image": 0.5}, {"image": 0.7})
    assert base.fingerprint != decide_route([_model("model-a")], other_requirements, hardware).fingerprint


def test_reason_codes_are_stable_and_sorted():
    hardware, requirements = _hardware(), _requirements()
    decision = decide_route([_model("model-a")], requirements, hardware)
    assert tuple(sorted(decision.reason_codes)) == decision.reason_codes
    assert "QUALIFIED" in decision.reason_codes and "HARDWARE_FIT" in decision.reason_codes
    assert f"HW:{hardware.fingerprint}" in decision.reason_codes
    assert f"REQ:{requirements.fingerprint}" in decision.reason_codes


def test_build_route_decision_rejects_mismatched_route_and_hardware():
    hardware = _hardware(available=7000)
    scored = choose_route([_model("model-a")], _requirements(), hardware)
    smaller = _hardware(available=1)
    with pytest.raises(ValueError):
        build_route_decision(scored, _requirements(), smaller)
