# GENERATED-DEEP-PREPROGRAMMED
class M21Error(Exception):
    retryable: bool = False

class ValidationFailure(M21Error): pass
class PolicyFailure(M21Error): pass
class CapabilityFailure(M21Error): retryable = True
class QualityFailure(M21Error): pass
class InvariantFailure(M21Error): pass
