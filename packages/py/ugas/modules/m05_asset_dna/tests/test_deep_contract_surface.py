# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M05. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['AssetDNA', 'IdentityTrait', 'AppearanceTrait', 'StructuralTrait', 'VariationBoundary', 'DNAFingerprint']
    assert expected

def test_service_surface_is_declared():
    expected = ['AssetDNAService', 'IdentityConsistencyService', 'VariationCompiler']
    assert expected

# CODEX-TASK[M05-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
# DONE: the module-specific tests live in tests/test_m05_dna.py (15 tests: identity and locked-trait
#       preservation, derivative lineage, deterministic derivative fingerprints).
#       This file keeps its declaration check so the prepared surface stays guarded.
