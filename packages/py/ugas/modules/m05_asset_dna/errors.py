# GENERATED-PREPROGRAMMED: architecture scaffold, not implemented production logic.
# Do not redesign ownership here. Follow planning canon + Context Pack.
"""Typed M05 domain/application failures with retryability metadata.

Retryability is not declared here. It is derived from the canonical kernel ErrorKind through
ugas.kernel.observability.is_retryable, so this module carries no competing retry taxonomy: the kernel
allow-list (transient, provider, resource) is the single source of truth, and STALE_STATE stays non-retryable.
"""
from ugas.kernel.observability import is_retryable
from ugas.kernel.primitives import ErrorKind


class ModuleError(Exception):
    """Base M05 failure. `kind` maps the failure onto the canonical kernel taxonomy."""

    kind: ErrorKind = ErrorKind.INTEGRITY_FAILURE

    @property
    def retryable(self) -> bool:
        return is_retryable(self.kind)


class ValidationError(ModuleError):
    kind = ErrorKind.INTEGRITY_FAILURE


class PolicyBlocked(ModuleError):
    kind = ErrorKind.POLICY_REJECTION


class QualityRejected(ModuleError):
    kind = ErrorKind.QUALITY_REJECTION


class CapabilityUnavailable(ModuleError):
    kind = ErrorKind.CAPABILITY_DENIED


class TransientUnavailable(ModuleError):
    kind = ErrorKind.TRANSIENT_FAILURE


class StaleState(ModuleError):
    kind = ErrorKind.STALE_STATE
