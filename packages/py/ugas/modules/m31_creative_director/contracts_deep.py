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
class CreativeIntentKernel(ContractBase):
    """Canonical M31 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CreativeConstraint(ContractBase):
    """Canonical M31 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CreativeDecision(ContractBase):
    """Canonical M31 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class VisualEmotionMap(ContractBase):
    """Canonical M31 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CreativeWorldModel(ContractBase):
    """Canonical M31 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class DirectionBrief(ContractBase):
    """Canonical M31 contract. Extend fields only from approved module canon."""
    pass

