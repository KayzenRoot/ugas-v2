from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True,slots=True)
class ExtensionManifest:
    id:str; version:str; api_version:str; entrypoint_ref:str; requested_capabilities:frozenset[str]; dependency_refs:tuple[str,...]; package_fingerprint:str
@dataclass(frozen=True,slots=True)
class HostCapabilities:
    api_version:str; granted_capabilities:frozenset[str]; supported_interfaces:frozenset[str]
@dataclass(frozen=True,slots=True)
class ExtensionGrant:
    extension_id:str; granted_capabilities:frozenset[str]; denied_capabilities:frozenset[str]; sandbox_profile_ref:str
@dataclass(frozen=True,slots=True)
class ExtensionInvocation:
    id:str; extension_id:str; interface:str; input_ref:str; required_capability:str; budget_ref:str
@dataclass(frozen=True,slots=True)
class ExtensionResult:
    invocation_ref:str; output_ref:str; evidence_ref:str; logs_ref:str; success:bool

# CODEX-TASK[M39-CONTRACT-EXPANSION]
# Add semver compatibility ranges, typed provider/tool/media interfaces, lifecycle hooks, resource budgets,
# signature/provenance metadata and migration contracts. No plugin gets ambient host authority.
