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
class SecurityPolicy(ContractBase):
    """Canonical M24 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class SecretRef(ContractBase):
    """Canonical M24 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class TrustBoundary(ContractBase):
    """Canonical M24 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class Permission(ContractBase):
    """Canonical M24 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AuditEvent(ContractBase):
    """Canonical M24 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ThreatFinding(ContractBase):
    """Canonical M24 contract. Extend fields only from approved module canon."""
    pass

