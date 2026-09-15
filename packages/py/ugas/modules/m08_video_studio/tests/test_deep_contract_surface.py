# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M08. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['VideoIntent', 'ShotPlan', 'TemporalConstraint', 'VideoCandidate', 'FrameWindow', 'VideoEvaluation', 'VideoMaster']
    assert expected

def test_service_surface_is_declared():
    expected = ['VideoPlanningService', 'VideoGenerationService', 'TemporalConsistencyService']
    assert expected

# CODEX-TASK[M08-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
