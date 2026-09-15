from ugas.media.contracts import ArtifactState, RuntimeDerivative, SpatialMaster, TargetCameraProfile
from ugas.spatial.acceptance import RuntimeBudget, SpatialAcceptancePolicy, SpatialGate, SpatialObservation, evaluate_spatial_derivative
from ugas.spatial.lod_policy import LodCandidate, LodPolicy, Representation, choose_cheapest_acceptable


def camera():
    return TargetCameraProfile("perspective", 45.0, 55.0, 12.0, 1920, 1080)


def master():
    return SpatialMaster("hero-master", "p", "fm", ArtifactState.ACCEPTED, None, (), "mesh", "topo", "uv", "mat")


def derivative(triangles=60000, texture_mb=256):
    return RuntimeDerivative("hero-runtime", "p", "fd", ArtifactState.ACCEPTED, None, ("hero-master",), "hero-master", camera(), triangles, texture_mb)


def test_target_camera_hard_gate_rejects_low_readability():
    policy = SpatialAcceptancePolicy({SpatialGate.SCREENSPACE_READABILITY:0.9, SpatialGate.IDENTITY:0.9}, camera(), RuntimeBudget(80000,512))
    decision = evaluate_spatial_derivative(master(), derivative(), SpatialObservation({SpatialGate.SCREENSPACE_READABILITY:0.7, SpatialGate.IDENTITY:0.95}), policy)
    assert not decision.accepted
    assert SpatialGate.SCREENSPACE_READABILITY in decision.failed_gates


def test_runtime_budget_is_hard_constraint():
    policy = SpatialAcceptancePolicy({}, camera(), RuntimeBudget(50000,128))
    decision = evaluate_spatial_derivative(master(), derivative(60000,256), SpatialObservation({}), policy)
    assert not decision.accepted
    assert SpatialGate.RUNTIME_BUDGET in decision.failed_gates


def test_cheapest_lod_must_still_preserve_perceptual_floor():
    policy = LodPolicy(0.10,0.90,0.85,0.90,100000,512)
    high = LodCandidate(Representation.HIGH,80000,400,0.01,0.99,0.98,0.99)
    medium = LodCandidate(Representation.MEDIUM,45000,220,0.05,0.95,0.91,0.95)
    low = LodCandidate(Representation.LOW,15000,80,0.08,0.70,0.80,0.75)
    assert choose_cheapest_acceptable([high,medium,low], policy) == medium


def test_source_master_mismatch_fails_closed():
    bad = RuntimeDerivative("d", "p", "fd", ArtifactState.ACCEPTED, None, ("other",), "other", camera(), 1, 1)
    decision = evaluate_spatial_derivative(master(), bad, SpatialObservation({}), SpatialAcceptancePolicy({}, camera(), RuntimeBudget(10,10)))
    assert not decision.accepted
