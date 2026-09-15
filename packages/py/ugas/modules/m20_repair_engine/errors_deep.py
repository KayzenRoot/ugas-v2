# GENERATED-DEEP-PREPROGRAMMED
class M20Error(Exception):
    retryable: bool = False

class ValidationFailure(M20Error): pass
class PolicyFailure(M20Error): pass
class CapabilityFailure(M20Error): retryable = True
class QualityFailure(M20Error): pass
class InvariantFailure(M20Error): pass
