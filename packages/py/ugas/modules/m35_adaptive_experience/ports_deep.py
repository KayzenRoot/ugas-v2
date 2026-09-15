# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class MasterProductionPort(Protocol):
    """M35 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class ConsentPolicyPort(Protocol):
    """M35 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class DeliveryMetricsPort(Protocol):
    """M35 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

