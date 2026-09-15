# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class ResearchSourcePort(Protocol):
    """M29 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class BenchmarkRunner(Protocol):
    """M29 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class SecurityReviewPort(Protocol):
    """M29 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class LicenseReviewPort(Protocol):
    """M29 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

