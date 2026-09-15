# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class NarrativePort(Protocol):
    """M15 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class MediaAssemblyPort(Protocol):
    """M15 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class DeliveryProfilePort(Protocol):
    """M15 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

