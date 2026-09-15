# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
from typing import Protocol
from .contracts import Command, Result

class CapabilityPort(Protocol):
    async def execute(self, command: Command) -> Result: ...
