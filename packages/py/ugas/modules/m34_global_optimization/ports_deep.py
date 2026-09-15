# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class ExecutionGraphPort(Protocol):
    """M34 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class HardwarePort(Protocol):
    """M34 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class BenchmarkPort(Protocol):
    """M34 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class EvidencePort(Protocol):
    """M34 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

