# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class MaterialInferencePort(Protocol):
    """M36 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class RendererPort(Protocol):
    """M36 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class DccPort(Protocol):
    """M36 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class AppearanceEvaluator(Protocol):
    """M36 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

