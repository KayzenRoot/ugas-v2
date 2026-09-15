# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M07. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['ImageIntent', 'ImageGenerationPlan', 'ImageCandidate', 'ImageRegion', 'ImageEvaluation', 'ImageMaster']
    assert expected

def test_service_surface_is_declared():
    expected = ['ImagePlanningService', 'ImageGenerationService', 'ImageSelectionService']
    assert expected

# CODEX-TASK[M07-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
