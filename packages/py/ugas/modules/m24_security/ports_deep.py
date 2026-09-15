# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class SecretStore(Protocol):
    """M24 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class AuditSink(Protocol):
    """M24 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class SecurityScanner(Protocol):
    """M24 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

