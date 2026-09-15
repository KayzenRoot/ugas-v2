# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class AgentRuntime(Protocol):
    """M27 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class ToolRegistry(Protocol):
    """M27 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class PolicyPort(Protocol):
    """M27 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

