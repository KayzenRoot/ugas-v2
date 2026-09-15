# GENERATED-DEEP-PREPROGRAMMED
class M16Error(Exception):
    retryable: bool = False

class ValidationFailure(M16Error): pass
class PolicyFailure(M16Error): pass
class CapabilityFailure(M16Error): retryable = True
class QualityFailure(M16Error): pass
class InvariantFailure(M16Error): pass
