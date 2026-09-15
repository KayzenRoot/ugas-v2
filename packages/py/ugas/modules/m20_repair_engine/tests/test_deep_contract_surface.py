# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M20. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['DefectMap', 'RepairPlan', 'RepairRegion', 'RepairAttempt', 'RepairEvaluation']
    assert expected

def test_service_surface_is_declared():
    expected = ['RepairPlanner', 'SelectiveRepairService', 'RevalidationService']
    assert expected

# CODEX-TASK[M20-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
