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
class ArtifactKey(ContractBase):
    """Canonical M25 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class BlobRef(ContractBase):
    """Canonical M25 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CacheKey(ContractBase):
    """Canonical M25 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CachePolicy(ContractBase):
    """Canonical M25 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ArtifactFingerprint(ContractBase):
    """Canonical M25 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class RetentionPolicy(ContractBase):
    """Canonical M25 contract. Extend fields only from approved module canon."""
    pass

