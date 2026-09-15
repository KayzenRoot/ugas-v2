# GENERATED-DEEP-PREPROGRAMMED
from typing import Any, Protocol

class VoiceProvider(Protocol):
    """M11 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class VoiceEvaluator(Protocol):
    """M11 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

class ConsentRegistry(Protocol):
    """M11 boundary. Provider/framework details stay behind this port."""
    async def execute(self, request: Any) -> Any: ...

