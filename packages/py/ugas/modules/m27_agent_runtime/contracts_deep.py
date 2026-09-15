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
class AgentRole(ContractBase):
    """Canonical M27 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AgentCapability(ContractBase):
    """Canonical M27 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AgentTask(ContractBase):
    """Canonical M27 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AgentDecision(ContractBase):
    """Canonical M27 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class ToolGrant(ContractBase):
    """Canonical M27 contract. Extend fields only from approved module canon."""
    pass

@dataclass(frozen=True, slots=True)
class AgentEvidence(ContractBase):
    """Canonical M27 contract. Extend fields only from approved module canon."""
    pass

