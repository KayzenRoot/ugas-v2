# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class RepairProvider(Protocol):
    """M20 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class DependencyGraphPort(Protocol):
    """M20 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class QualityCourtPort(Protocol):
    """M20 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

