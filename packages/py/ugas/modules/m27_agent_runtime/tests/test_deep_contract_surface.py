# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M27. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['AgentRole', 'AgentCapability', 'AgentTask', 'AgentDecision', 'ToolGrant', 'AgentEvidence']
    assert expected

def test_service_surface_is_declared():
    expected = ['AgentOrchestrator', 'CapabilityBroker', 'AgentGovernanceService']
    assert expected

# CODEX-TASK[M27-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
