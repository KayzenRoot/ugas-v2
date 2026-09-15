# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class EventStream(Protocol):
    """M26 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class MetricsStore(Protocol):
    """M26 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class ControlPlanePort(Protocol):
    """M26 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

