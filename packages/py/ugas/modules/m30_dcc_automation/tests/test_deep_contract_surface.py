# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M30. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['DccIR', 'DccOperation', 'SemanticSelector', 'DccTransaction', 'DccJob', 'DccResult', 'SceneFingerprint']
    assert expected

def test_service_surface_is_declared():
    expected = ['DccCompiler', 'SceneTransactionEngine', 'BlenderWorkerService', 'DccQualityDossierService']
    assert expected

# CODEX-TASK[M30-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
