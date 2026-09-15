# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class ObjectStore(Protocol):
    """M25 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class CacheBackend(Protocol):
    """M25 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class MetadataRepository(Protocol):
    """M25 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

