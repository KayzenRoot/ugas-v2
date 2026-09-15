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
class MusicIntent(ContractBase):
    """Canonical M12 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CuePlan(ContractBase):
    """Canonical M12 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class StemSet(ContractBase):
    """Canonical M12 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class MusicCandidate(ContractBase):
    """Canonical M12 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class MusicEvaluation(ContractBase):
    """Canonical M12 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class MusicMaster(ContractBase):
    """Canonical M12 contract. Extend fields only from approved module canon."""
    pass

