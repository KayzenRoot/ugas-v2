# GENERATED-DEEP-PREPROGRAMMED
class M22Error(Exception):
    retryable: bool = False

class ValidationFailure(M22Error): pass
class PolicyFailure(M22Error): pass
class CapabilityFailure(M22Error): retryable = True
class QualityFailure(M22Error): pass
class InvariantFailure(M22Error): pass
