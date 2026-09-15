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
class IRDocument(ContractBase):
    """Canonical M04 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class IRNode(ContractBase):
    """Canonical M04 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class IRReference(ContractBase):
    """Canonical M04 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class Modality(ContractBase):
    """Canonical M04 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class Constraint(ContractBase):
    """Canonical M04 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class IntentLock(ContractBase):
    """Canonical M04 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class IRVersion(ContractBase):
    """Canonical M04 contract. Extend fields only from approved module canon."""
    pass

