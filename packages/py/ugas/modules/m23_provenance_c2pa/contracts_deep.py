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
class ProvenanceRecord(ContractBase):
    """Canonical M23 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class RightsRecord(ContractBase):
    """Canonical M23 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class TransformationRecord(ContractBase):
    """Canonical M23 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ContentCredential(ContractBase):
    """Canonical M23 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class LineageEdge(ContractBase):
    """Canonical M23 contract. Extend fields only from approved module canon."""
    pass

