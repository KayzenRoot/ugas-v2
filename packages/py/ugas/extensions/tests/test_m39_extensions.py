from ugas.extensions.contracts import *
from ugas.extensions.runtime import authorize_invocation,negotiate

def manifest(caps=frozenset({"media.read"})): return ExtensionManifest("x","1.0.0","v1","entry",caps,(),"sha")
def host(): return HostCapabilities("v1",frozenset({"media.read"}),frozenset({"media.provider"}))

def test_ungranted_capability_is_denied_by_default():
    g=negotiate(manifest(frozenset({"media.read","network"})),host(),sandbox_profile_ref="restricted")
    assert g.granted_capabilities==frozenset({"media.read"}); assert g.denied_capabilities==frozenset({"network"})

def test_invocation_cannot_escalate_capability():
    g=negotiate(manifest(),host(),sandbox_profile_ref="restricted")
    i=ExtensionInvocation("i","x","media.provider","input","network","budget")
    try: authorize_invocation(i,g,host())
    except PermissionError as exc: assert "capability" in str(exc)
    else: raise AssertionError("must fail")

def test_api_mismatch_fails_closed():
    try: negotiate(manifest(),HostCapabilities("v2",frozenset(),frozenset()),sandbox_profile_ref="restricted")
    except ValueError as exc: assert "version" in str(exc)
    else: raise AssertionError("must fail")

# CODEX-TASK[M39-A2]
# Add compatibility matrix, signed-package provenance, sandbox escape negative fixtures, budget exhaustion,
# deterministic plugin lifecycle and migration tests. No external plugin process required in A1/A2.
