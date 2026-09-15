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
class DeliveryTarget(ContractBase):
    """Canonical M28 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class DeliveryProfile(ContractBase):
    """Canonical M28 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ExportPlan(ContractBase):
    """Canonical M28 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class DeliveryPackage(ContractBase):
    """Canonical M28 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class DeliveryReceipt(ContractBase):
    """Canonical M28 contract. Extend fields only from approved module canon."""
    pass

