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
class CostEstimate(ContractBase):
    """Canonical M21 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class RenderPlan(ContractBase):
    """Canonical M21 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class RouteEconomics(ContractBase):
    """Canonical M21 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class BudgetEnvelope(ContractBase):
    """Canonical M21 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class FailureAdjustedCost(ContractBase):
    """Canonical M21 contract. Extend fields only from approved module canon."""
    pass

