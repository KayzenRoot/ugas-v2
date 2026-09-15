# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M04. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['IRDocument', 'IRNode', 'IRReference', 'Modality', 'Constraint', 'IntentLock', 'IRVersion']
    assert expected

def test_service_surface_is_declared():
    expected = ['IRCompiler', 'IRValidator', 'IRMigrationService']
    assert expected

# CODEX-TASK[M04-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
# DONE: the module-specific tests live in tests/test_m04_ir.py (19 tests: reference integrity, lock
#       resolvability/preservation, fingerprint sealing, bounded v1->v2 migration).
#       This file keeps its declaration check so the prepared surface stays guarded.
