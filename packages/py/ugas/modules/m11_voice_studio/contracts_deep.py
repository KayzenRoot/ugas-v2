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
class VoiceIdentity(ContractBase):
    """Canonical M11 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class VoiceIntent(ContractBase):
    """Canonical M11 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class UtterancePlan(ContractBase):
    """Canonical M11 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class VoiceCandidate(ContractBase):
    """Canonical M11 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class VoiceEvaluation(ContractBase):
    """Canonical M11 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class VoiceMaster(ContractBase):
    """Canonical M11 contract. Extend fields only from approved module canon."""
    pass

