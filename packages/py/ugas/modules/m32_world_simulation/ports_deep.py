# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class PhysicsPort(Protocol):
    """M32 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class EnvironmentPort(Protocol):
    """M32 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class ActorSimulationPort(Protocol):
    """M32 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class StateRepository(Protocol):
    """M32 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

