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
class DccIR(ContractBase):
    """Canonical M30 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class DccOperation(ContractBase):
    """Canonical M30 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class SemanticSelector(ContractBase):
    """Canonical M30 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class DccTransaction(ContractBase):
    """Canonical M30 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class DccJob(ContractBase):
    """Canonical M30 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class DccResult(ContractBase):
    """Canonical M30 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class SceneFingerprint(ContractBase):
    """Canonical M30 contract. Extend fields only from approved module canon."""
    pass

