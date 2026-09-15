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
class ExperienceIR(ContractBase):
    """Canonical M35 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AudienceContext(ContractBase):
    """Canonical M35 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class CreativeInvariantLock(ContractBase):
    """Canonical M35 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AdaptiveVariant(ContractBase):
    """Canonical M35 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ExperimentPlan(ContractBase):
    """Canonical M35 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ExperienceEvaluation(ContractBase):
    """Canonical M35 contract. Extend fields only from approved module canon."""
    pass

