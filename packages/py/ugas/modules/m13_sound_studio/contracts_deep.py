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
class SoundIntent(ContractBase):
    """Canonical M13 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class FoleyEvent(ContractBase):
    """Canonical M13 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AmbienceBed(ContractBase):
    """Canonical M13 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class SfxAsset(ContractBase):
    """Canonical M13 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AudioScene(ContractBase):
    """Canonical M13 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class SoundEvaluation(ContractBase):
    """Canonical M13 contract. Extend fields only from approved module canon."""
    pass

