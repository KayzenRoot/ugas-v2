# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.

# CODEX-TASK[M29-CORE]
# WHAT: complete only the bounded technology candidates/Golden Shards/benchmarks/qualification behavior described by this module's planning canon.
# INPUT: typed contracts from contracts.py and canonical shared primitives.
# OUTPUT: typed result/events plus evidence references; never raw provider state as domain truth.
# INVARIANTS: provider-independent intent; deterministic lineage; hard gates preserved; delta proof reuse.
# ERRORS: use typed failures from errors.py; mark retryability explicitly.
# TEST: tests/test_contracts.py then tests/test_service.py; broader suites only via Test Impact Graph.
# DONE: focused tests pass and no unresolved CORE task remains.

from .contracts import Command, Result
from .domain import validate_invariants

class Service:
    def __init__(self, capability): self._capability = capability
    async def execute(self, command: Command) -> Result:
        command = validate_invariants(command)
        # CODEX-TASK: implement module-specific orchestration; do not add provider SDK imports.
        return await self._capability.execute(command)
