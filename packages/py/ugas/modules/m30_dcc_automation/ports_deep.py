# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class DccAdapter(Protocol):
    """M30 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class BlenderHeadlessPort(Protocol):
    """M30 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class RendererPort(Protocol):
    """M30 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class ArtifactStore(Protocol):
    """M30 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

