# GENERATED-DEEP-PREPROGRAMMED
class M09Error(Exception):
    retryable: bool = False

class ValidationFailure(M09Error): pass
class PolicyFailure(M09Error): pass
class CapabilityFailure(M09Error): retryable = True
class QualityFailure(M09Error): pass
class InvariantFailure(M09Error): pass
