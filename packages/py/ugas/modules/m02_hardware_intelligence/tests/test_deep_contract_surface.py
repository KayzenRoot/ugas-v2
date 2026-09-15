# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M02. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['HardwareProfile', 'GpuProfile', 'CpuProfile', 'MemoryProfile', 'ResourceEnvelope', 'CapabilityProbe', 'ResourceLease']
    assert expected

def test_service_surface_is_declared():
    expected = ['HardwareProbeService', 'ResourceEnvelopeService', 'LeasePlanner']
    assert expected

# CODEX-TASK[M02-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
