from ugas.kernel.adapter_qualification import AdapterQualification,AdapterState,assert_usable,requalify_on_version_change
from ugas.kernel.evidence_graph import EvidenceGraph,EvidenceNode,ProofState,carry_forward,detect_cycles,graph_fingerprint,invalidate,record_dependency_fingerprints,validate_graph
from ugas.kernel.observability import FailureRecord,OperationTelemetry,assert_secret_free,is_retryable,redact_secrets,validate_failure,validate_telemetry
from ugas.kernel.primitives import ErrorKind
import pytest

def test_evidence_invalidation_is_causal_not_global():
    g=EvidenceGraph("p",(
        EvidenceNode("a","p","asset:v1","identity",ProofState.PROVEN,"m06",(),"proof:a"),
        EvidenceNode("b","p","video:v1","temporal",ProofState.PROVEN,"m08",("a",),"proof:b"),
        EvidenceNode("c","p","audio:v1","voice",ProofState.PROVEN,"m11",(),"proof:c"),))
    validate_graph(g); out=invalidate(g,{"asset:v1"}); states={n.id:n.state for n in out.nodes}
    assert states["a"] is ProofState.INVALIDATED and states["b"] is ProofState.INVALIDATED
    assert states["c"] is ProofState.PROVEN

def test_adapter_requires_qualification_and_evidence():
    q=AdapterQualification("q","blender","blender","5.x",AdapterState.CANDIDATE,frozenset({"dcc.headless"}),"lic","sec","bench","hw","compat")
    try: assert_usable(q,frozenset({"dcc.headless"}))
    except PermissionError: pass
    else: raise AssertionError("candidate adapter must fail closed")

def test_policy_rejection_cannot_be_retryable():
    r=FailureRecord("f","p","trace","op",ErrorKind.POLICY_REJECTION,True,"rights_denied","evidence")
    try: validate_failure(r)
    except ValueError as exc: assert "non-retryable" in str(exc)
    else: raise AssertionError("must fail")

# ---------------------------------------------------------------------------
# CODEX-TASK[KERNEL-A1]: cycle detection, carry-forward fingerprint checks,
# adapter version invalidation, secret redaction, retry fixtures.
# Dependency-light: kernel only, no GPU/network/provider access.
# ---------------------------------------------------------------------------

def _qualified(version="5.x",capabilities=frozenset({"dcc.headless"})):
    return AdapterQualification("q","blender","blender",version,AdapterState.QUALIFIED,capabilities,"lic","sec","bench","hw","compat")

def _chain():
    return EvidenceGraph("p",(
        EvidenceNode("a","p","asset:v1","identity",ProofState.PROVEN,"m06",(),"proof:a"),
        EvidenceNode("b","p","video:v1","temporal",ProofState.PROVEN,"m08",("a",),"proof:b"),))

def test_cycle_is_detected_and_rejected():
    cyc=EvidenceGraph("p",(
        EvidenceNode("a","p","asset:v1","identity",ProofState.PROVEN,"m06",("b",),"proof:a"),
        EvidenceNode("b","p","video:v1","temporal",ProofState.PROVEN,"m08",("a",),"proof:b"),))
    assert detect_cycles(cyc)==(("a","b"),)
    try: validate_graph(cyc)
    except ValueError as exc: assert "cyclic" in str(exc)
    else: raise AssertionError("cyclic evidence graph must not validate")

def test_self_dependency_is_a_cycle():
    assert detect_cycles(EvidenceGraph("p",(EvidenceNode("a","p","x","identity",ProofState.PROVEN,"m06",("a",),"proof:a"),)))==(("a",),)

def test_acyclic_graph_reports_no_cycles():
    assert detect_cycles(_chain())==()

def test_graph_fingerprint_is_order_independent_and_content_sensitive():
    a,b=_chain().nodes
    assert graph_fingerprint(EvidenceGraph("p",(a,b)))==graph_fingerprint(EvidenceGraph("p",(b,a)))
    assert graph_fingerprint(EvidenceGraph("p",(a,b)))!=graph_fingerprint(invalidate(EvidenceGraph("p",(a,b)),{"asset:v1"}))

def test_carry_forward_requires_unchanged_dependency_fingerprints():
    snapshot=record_dependency_fingerprints(_chain())
    same={n.id:n.subject_fingerprint for n in snapshot.nodes}
    out={n.id:n.state for n in carry_forward(snapshot,same).nodes}
    assert out["a"] is ProofState.CARRY_FORWARD and out["b"] is ProofState.CARRY_FORWARD
    changed=dict(same); changed["a"]="asset:v2"
    out2={n.id:n.state for n in carry_forward(snapshot,changed).nodes}
    assert out2["a"] is ProofState.INVALIDATED, "a node whose own subject changed is not unchanged proof"
    assert out2["b"] is ProofState.INVALIDATED, "dependent proof must not carry forward"

def test_carry_forward_rejects_own_subject_change_without_dependents():
    g=EvidenceGraph("p",(
        EvidenceNode("a","p","asset:v1","identity",ProofState.PROVEN,"m06",(),"proof:a"),
        EvidenceNode("c","p","audio:v1","voice",ProofState.PROVEN,"m11",(),"proof:c"),))
    snapshot=record_dependency_fingerprints(g)
    out={n.id:n.state for n in carry_forward(snapshot,{"a":"asset:v2","c":"audio:v1"}).nodes}
    assert out["a"] is ProofState.INVALIDATED, "own subject change invalidates even with no dependents"
    assert out["c"] is ProofState.CARRY_FORWARD, "an unrelated independent proof still carries forward"

def test_carry_forward_fails_closed_without_dependency_snapshot():
    out={n.id:n.state for n in carry_forward(_chain(),{"a":"asset:v1","b":"video:v1"}).nodes}
    assert out["b"] is ProofState.INVALIDATED and out["a"] is ProofState.CARRY_FORWARD

def test_carry_forward_fails_closed_when_own_fingerprint_is_unverifiable():
    snapshot=record_dependency_fingerprints(_chain())
    out={n.id:n.state for n in carry_forward(snapshot,{}).nodes}
    assert out["a"] is ProofState.INVALIDATED and out["b"] is ProofState.INVALIDATED, "unverifiable fingerprints are never unchanged proofs"

def test_carry_forward_never_promotes_unproven_states():
    g=EvidenceGraph("p",(EvidenceNode("a","p","x","identity",ProofState.UNKNOWN,"m06"),))
    assert carry_forward(g,{}).nodes[0].state is ProofState.UNKNOWN

def test_adapter_version_mismatch_fails_closed():
    q=_qualified(version="5.x")
    assert_usable(q,frozenset({"dcc.headless"}),requested_version="5.x")
    try: assert_usable(q,frozenset({"dcc.headless"}),requested_version="6.x")
    except PermissionError as exc: assert "version mismatch" in str(exc)
    else: raise AssertionError("version-specific qualification must fail closed")

def test_version_change_returns_adapter_to_candidate():
    q=_qualified(version="5.x")
    changed,invalidated=requalify_on_version_change(q,"6.x")
    assert changed.state is AdapterState.CANDIDATE and changed.version=="6.x"
    assert invalidated==frozenset({"dcc.headless"}), "only dependent capabilities invalidate"
    same,cleared=requalify_on_version_change(q,"5.x")
    assert same is q and cleared==frozenset(), "unchanged version is a no-op"

def test_qualified_adapter_missing_evidence_fails_closed():
    q=AdapterQualification("q","blender","blender","5.x",AdapterState.QUALIFIED,frozenset({"dcc.headless"}),"","sec","bench","hw","compat")
    try: assert_usable(q,frozenset({"dcc.headless"}))
    except ValueError as exc: assert "qualification evidence" in str(exc)
    else: raise AssertionError("missing qualification evidence must fail closed")

def test_retry_classification_never_retries_hard_rejections():
    for kind in (ErrorKind.POLICY_REJECTION,ErrorKind.QUALITY_REJECTION,ErrorKind.CAPABILITY_DENIED,ErrorKind.INTEGRITY_FAILURE):
        assert is_retryable(kind) is False, f"{kind} must never be retryable"

def test_transient_provider_and_resource_failures_are_retryable():
    for kind in (ErrorKind.TRANSIENT_FAILURE,ErrorKind.PROVIDER_FAILURE,ErrorKind.RESOURCE_EXHAUSTED):
        assert is_retryable(kind) is True, f"{kind} must be a generic retry candidate"

def test_stale_state_is_not_generically_retryable():
    """A stale state needs reconciliation/refetch/new causal state before retry, so it fails closed."""
    assert is_retryable(ErrorKind.STALE_STATE) is False
    r=FailureRecord("f","p","trace","op",ErrorKind.STALE_STATE,True,"stale","evidence")
    try: validate_failure(r)
    except ValueError as exc: assert "non-retryable" in str(exc)
    else: raise AssertionError("STALE_STATE must not be marked retryable")

def test_retry_allowlist_is_exhaustive_over_error_kinds():
    """Every ErrorKind is classified; only the three allow-listed kinds are retry candidates."""
    assert {k for k in ErrorKind if is_retryable(k)}=={ErrorKind.TRANSIENT_FAILURE,ErrorKind.PROVIDER_FAILURE,ErrorKind.RESOURCE_EXHAUSTED}
    assert {k for k in ErrorKind if not is_retryable(k)}=={ErrorKind.POLICY_REJECTION,ErrorKind.QUALITY_REJECTION,ErrorKind.CAPABILITY_DENIED,ErrorKind.INTEGRITY_FAILURE,ErrorKind.STALE_STATE}

def test_secret_like_keys_are_rejected_and_redacted():
    payload={"operation":"render","api_key":"sk-live-123"}
    assert assert_secret_free({"operation":"render"}) is None
    try: assert_secret_free(payload)
    except ValueError as exc: assert "api_key" in str(exc)
    else: raise AssertionError("secret-like key must be rejected")
    safe=redact_secrets(payload)
    assert safe["api_key"]=="***REDACTED***" and safe["operation"]=="render"

def test_nested_secret_keys_are_rejected_and_redacted():
    """The boundary must not stop at the top level: a nested structured secret must be caught."""
    payload={"operation":"render","nested":{"token":"abc"},"deep":{"a":{"b":{"client_secret":"x"}}}}
    try: assert_secret_free(payload)
    except ValueError as exc: assert "nested.token" in str(exc)
    else: raise AssertionError("nested secret-like key must be rejected")
    safe=redact_secrets(payload)
    assert safe["nested"]["token"]=="***REDACTED***" and safe["nested"] is not payload["nested"]
    assert safe["deep"]["a"]["b"]["client_secret"]=="***REDACTED***"
    assert safe["operation"]=="render", "non-secret structure must be preserved"

def test_secret_in_sequence_of_mappings_is_rejected_and_redacted():
    payload={"attempts":[{"provider":"a"},{"authorization":"Bearer xyz"}],"note":"ok"}
    try: assert_secret_free(payload)
    except ValueError as exc: assert "attempts[1].authorization" in str(exc)
    else: raise AssertionError("a secret-like key inside a sequence must be rejected")
    safe=redact_secrets(payload)
    assert safe["attempts"][1]["authorization"]=="***REDACTED***"
    assert safe["attempts"][0]["provider"]=="a" and safe["note"]=="ok"
    assert isinstance(safe["attempts"],list), "container types must be preserved"

def test_redaction_preserves_tuple_containers():
    safe=redact_secrets({"pair":({"password":"x"},{"token":"y"})})
    assert isinstance(safe["pair"],tuple) and safe["pair"][0]["password"]=="***REDACTED***" and safe["pair"][1]["token"]=="***REDACTED***"

def test_secret_free_assertion_is_required_on_failure_records():
    r=FailureRecord("f","p","trace","op",ErrorKind.TRANSIENT_FAILURE,True,"timeout","evidence",secret_free=False)
    try: validate_failure(r)
    except ValueError as exc: assert "secrets" in str(exc)
    else: raise AssertionError("non-secret-free record must be rejected")

def test_telemetry_requires_trace_and_evidence_correlation():
    ok=OperationTelemetry("p","trace","op",10,1.0,0.0,128,0,0.5,"evidence")
    assert validate_telemetry(ok) is None
    for bad in (OperationTelemetry("p","","op",10,1.0,0.0,128,0,0.5,"evidence"),
                OperationTelemetry("p","trace","op",10,1.0,0.0,128,0,0.5,""),
                OperationTelemetry("p","trace","op",-1,1.0,0.0,128,0,0.5,"evidence")):
        try: validate_telemetry(bad)
        except ValueError: pass
        else: raise AssertionError("invalid telemetry must fail closed")

# CODEX-TASK[KERNEL-A1]
# Remaining: fixtures for the OpenTelemetry exporter adapter once KERNEL-OTEL-BRIDGE lands, and the
# KERNEL-ADAPTER-REGISTRY cross-module suite once that registry exists.
