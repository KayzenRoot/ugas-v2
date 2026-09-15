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
class VideoIntent(ContractBase):
    """Canonical M08 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ShotPlan(ContractBase):
    """Canonical M08 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class TemporalConstraint(ContractBase):
    """Canonical M08 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class VideoCandidate(ContractBase):
    """Canonical M08 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class FrameWindow(ContractBase):
    """Canonical M08 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class VideoEvaluation(ContractBase):
    """Canonical M08 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class VideoMaster(ContractBase):
    """Canonical M08 contract. Extend fields only from approved module canon."""
    pass

