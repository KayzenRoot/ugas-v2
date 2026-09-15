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
class AppearanceIR(ContractBase):
    """Canonical M36 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class MaterialObservation(ContractBase):
    """Canonical M36 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class NeuralMaterial(ContractBase):
    """Canonical M36 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AnalyticMaterial(ContractBase):
    """Canonical M36 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class LightingEstimate(ContractBase):
    """Canonical M36 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AppearanceDerivative(ContractBase):
    """Canonical M36 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AppearanceEvaluation(ContractBase):
    """Canonical M36 contract. Extend fields only from approved module canon."""
    pass

