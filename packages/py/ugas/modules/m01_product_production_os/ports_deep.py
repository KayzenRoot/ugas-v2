# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class MetadataRepository(Protocol):
    """M01 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class EventBus(Protocol):
    """M01 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class EvidenceSink(Protocol):
    """M01 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class Clock(Protocol):
    """M01 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

