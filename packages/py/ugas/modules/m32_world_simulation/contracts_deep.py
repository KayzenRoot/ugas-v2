# GENERATED-DEEP-PREPROGRAMMED
from dataclasses import dataclass, field
from typing import Any, Mapping

@dataclass(frozen=True, slots=True)
class ContractBase:
    id: str
    version: int = 1
    fingerprint: str = ''
    metadata: Mapping[str, Any] = field(default_factory=dict)

@dataclass(frozen=True, slots=True)
class WorldState(ContractBase):
    """Canonical M32 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class WorldSnapshot(ContractBase):
    """Canonical M32 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class SpatialState(ContractBase):
    """Canonical M32 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class TemporalState(ContractBase):
    """Canonical M32 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ActorState(ContractBase):
    """Canonical M32 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CausalEvent(ContractBase):
    """Canonical M32 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class SimulationBranch(ContractBase):
    """Canonical M32 contract. Extend fields only from approved module canon."""
    pass

