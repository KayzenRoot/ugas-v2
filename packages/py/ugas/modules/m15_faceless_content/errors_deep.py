# GENERATED-DEEP-PREPROGRAMMED
class M15Error(Exception):
    retryable: bool = False

class ValidationFailure(M15Error): pass
class PolicyFailure(M15Error): pass
class CapabilityFailure(M15Error): retryable = True
class QualityFailure(M15Error): pass
class InvariantFailure(M15Error): pass
