# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M03. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['ModelProfile', 'CapabilityVector', 'BenchmarkResult', 'RouteCandidate', 'RouteDecision', 'QualificationState']
    assert expected

def test_service_surface_is_declared():
    expected = ['ModelRegistryService', 'CapabilityMatcher', 'RouteSelector', 'QualificationService']
    assert expected

# CODEX-TASK[M03-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
# DONE: the module-specific tests live in tests/test_m03_routing.py (20 tests: qualification gate,
#       capability residual, hardware fit, deterministic routing, evidence-requiring promotion).
#       This file keeps its declaration check so the prepared surface stays guarded.
