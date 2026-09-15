# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class Exporter(Protocol):
    """M28 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class PlatformAdapter(Protocol):
    """M28 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class ArtifactStore(Protocol):
    """M28 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

