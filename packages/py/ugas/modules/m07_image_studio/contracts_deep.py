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
class ImageIntent(ContractBase):
    """Canonical M07 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ImageGenerationPlan(ContractBase):
    """Canonical M07 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ImageCandidate(ContractBase):
    """Canonical M07 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ImageRegion(ContractBase):
    """Canonical M07 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ImageEvaluation(ContractBase):
    """Canonical M07 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ImageMaster(ContractBase):
    """Canonical M07 contract. Extend fields only from approved module canon."""
    pass

