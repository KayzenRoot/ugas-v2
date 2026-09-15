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
class ProductionSessionIR(ContractBase):
    """Canonical M33 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class StageState(ContractBase):
    """Canonical M33 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CameraPlan(ContractBase):
    """Canonical M33 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class LightingState(ContractBase):
    """Canonical M33 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class PerformanceIntent(ContractBase):
    """Canonical M33 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class Take(ContractBase):
    """Canonical M33 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CoverageGraph(ContractBase):
    """Canonical M33 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class EditCandidate(ContractBase):
    """Canonical M33 contract. Extend fields only from approved module canon."""
    pass

