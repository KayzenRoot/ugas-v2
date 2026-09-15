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
class DefectMap(ContractBase):
    """Canonical M20 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class RepairPlan(ContractBase):
    """Canonical M20 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class RepairRegion(ContractBase):
    """Canonical M20 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class RepairAttempt(ContractBase):
    """Canonical M20 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class RepairEvaluation(ContractBase):
    """Canonical M20 contract. Extend fields only from approved module canon."""
    pass

