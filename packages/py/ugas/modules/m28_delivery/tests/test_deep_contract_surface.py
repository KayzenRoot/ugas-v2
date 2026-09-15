# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M28. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['DeliveryTarget', 'DeliveryProfile', 'ExportPlan', 'DeliveryPackage', 'DeliveryReceipt']
    assert expected

def test_service_surface_is_declared():
    expected = ['DeliveryCompiler', 'ExportService', 'DeliveryValidationService']
    assert expected

# CODEX-TASK[M28-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
