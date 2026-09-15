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
class MotionIntent(ContractBase):
    """Canonical M09 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class SkeletonBinding(ContractBase):
    """Canonical M09 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class MotionClip(ContractBase):
    """Canonical M09 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class MotionConstraint(ContractBase):
    """Canonical M09 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class RetargetPlan(ContractBase):
    """Canonical M09 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AnimationEvaluation(ContractBase):
    """Canonical M09 contract. Extend fields only from approved module canon."""
    pass

