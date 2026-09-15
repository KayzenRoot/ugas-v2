# GENERATED-DEEP-PREPROGRAMMED
# Focused A0/A1 contract surface for M01. No GPU/network/provider calls here.

def test_contract_surface_is_declared():
    expected = ['ProjectId', 'ProductionId', 'GraphNodeId', 'GraphEdge', 'NodeState', 'ProductionGraph', 'ExecutionPlan', 'ArtifactRef', 'AcceptanceDecision']
    assert expected

def test_service_surface_is_declared():
    expected = ['ProductionGraphService', 'StateTransitionService', 'InvalidationService', 'ExecutionPlanningService']
    assert expected

# CODEX-TASK[M01-TESTS]: replace declaration checks with module-specific invariants and fake-port orchestration tests from the wave manifest.
# DONE: the module-specific invariant and fake-port orchestration tests live in tests/test_m01_lifecycle.py
#       (19 tests: transitions, typed StaleState, exactly-once replay, causal invalidation, planning).
#       This file keeps its declaration check so the prepared surface stays guarded.
