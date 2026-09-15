# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class PricingRegistry(Protocol):
    """M21 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class HardwarePort(Protocol):
    """M21 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class ModelIntelligencePort(Protocol):
    """M21 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

