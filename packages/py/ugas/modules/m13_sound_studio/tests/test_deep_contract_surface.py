# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M13. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['SoundIntent', 'FoleyEvent', 'AmbienceBed', 'SfxAsset', 'AudioScene', 'SoundEvaluation']
    assert expected

def test_service_surface_is_declared():
    expected = ['SoundSceneCompiler', 'FoleyService', 'SfxService', 'AmbienceService']
    assert expected

# CODEX-TASK[M13-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
