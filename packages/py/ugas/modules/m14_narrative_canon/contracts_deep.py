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
class CanonState(ContractBase):
    """Canonical M14 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CharacterState(ContractBase):
    """Canonical M14 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class WorldFact(ContractBase):
    """Canonical M14 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class NarrativeBeat(ContractBase):
    """Canonical M14 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class SceneIntent(ContractBase):
    """Canonical M14 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ContinuityConstraint(ContractBase):
    """Canonical M14 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class NarrativeDecision(ContractBase):
    """Canonical M14 contract. Extend fields only from approved module canon."""
    pass

