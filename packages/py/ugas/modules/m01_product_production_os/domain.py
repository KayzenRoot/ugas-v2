# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.

# CODEX-TASK[M01-CORE]
# WHAT: complete only the bounded production graph/state machine/recipes/snapshots/invalidation/scheduling behavior described by this module's planning canon.
# INPUT: typed contracts from contracts.py and canonical shared primitives.
# OUTPUT: typed result/events plus evidence references; never raw provider state as domain truth.
# INVARIANTS: provider-independent intent; deterministic lineage; hard gates preserved; delta proof reuse.
# ERRORS: use typed failures from errors.py; mark retryability explicitly.
# TEST: tests/test_contracts.py then tests/test_service.py; broader suites only via Test Impact Graph.
# DONE: focused tests pass and no unresolved CORE task remains.

def validate_invariants(command):
    # CODEX-TASK: replace with module-specific pure invariant checks from planning canon.
    if not command.operation:
        raise ValueError('operation is required')
    return command
