# GENERATED-DEEP-PREPROGRAMMED
class M06Error(Exception):
    retryable: bool = False

class ValidationFailure(M06Error): pass
class PolicyFailure(M06Error): pass
class CapabilityFailure(M06Error): retryable = True
class QualityFailure(M06Error): pass
class InvariantFailure(M06Error): pass
