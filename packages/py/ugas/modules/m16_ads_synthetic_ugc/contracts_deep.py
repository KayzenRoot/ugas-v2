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
class CampaignIntent(ContractBase):
    """Canonical M16 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class Claim(ContractBase):
    """Canonical M16 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class EvidenceBinding(ContractBase):
    """Canonical M16 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AdConcept(ContractBase):
    """Canonical M16 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class UGCVariant(ContractBase):
    """Canonical M16 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ConversionObjective(ContractBase):
    """Canonical M16 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AdEvaluation(ContractBase):
    """Canonical M16 contract. Extend fields only from approved module canon."""
    pass

