from __future__ import annotations
from .contracts import ExtensionGrant,ExtensionInvocation,ExtensionManifest,HostCapabilities

def negotiate(manifest:ExtensionManifest,host:HostCapabilities,*,sandbox_profile_ref:str)->ExtensionGrant:
    if manifest.api_version!=host.api_version: raise ValueError("extension API version mismatch")
    granted=manifest.requested_capabilities & host.granted_capabilities
    denied=manifest.requested_capabilities-granted
    if not sandbox_profile_ref: raise ValueError("extension sandbox profile required")
    return ExtensionGrant(manifest.id,frozenset(granted),frozenset(denied),sandbox_profile_ref)

def authorize_invocation(invocation:ExtensionInvocation,grant:ExtensionGrant,host:HostCapabilities)->None:
    if invocation.extension_id!=grant.extension_id: raise PermissionError("extension grant mismatch")
    if invocation.interface not in host.supported_interfaces: raise PermissionError("extension interface unsupported")
    if invocation.required_capability not in grant.granted_capabilities: raise PermissionError("extension capability denied")
    if not invocation.budget_ref: raise ValueError("extension invocation requires resource budget")

# CODEX-TASK[M39-SANDBOX-RUNTIME]
# Implement process/WASM/container isolation adapters only after M29 qualification. Enforce filesystem,
# network, GPU, secret and tool scopes independently; capability denial must be default and auditable.
