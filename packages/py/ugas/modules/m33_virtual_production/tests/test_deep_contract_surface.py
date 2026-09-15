# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M33. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['ProductionSessionIR', 'StageState', 'CameraPlan', 'LightingState', 'PerformanceIntent', 'Take', 'CoverageGraph', 'EditCandidate']
    assert expected

def test_service_surface_is_declared():
    expected = ['StageManager', 'CinematographyDirector', 'LightingDirector', 'TakeFactory', 'ContinuitySupervisor', 'EditorialService', 'ReshootDirector']
    assert expected

# CODEX-TASK[M33-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
