# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
"""M03 capability protocols. Provider and framework details stay behind these ports."""
from typing import Protocol

from ugas.foundation.contracts import ModelProfile

from .contracts import Command, Result


class CapabilityPort(Protocol):
    async def execute(self, command: Command) -> Result: ...


class ModelRegistryPort(Protocol):
    """In-memory or adapter-backed store of qualified model profiles. No provider call is implied."""

    async def put(self, profile: ModelProfile) -> None: ...
    async def get(self, model_key: str) -> ModelProfile | None: ...
    async def all(self) -> tuple[ModelProfile, ...]: ...
