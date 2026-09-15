# GENERATED-DEEP-PREPROGRAMMED
class M07Error(Exception):
    retryable: bool = False

class ValidationFailure(M07Error): pass
class PolicyFailure(M07Error): pass
class CapabilityFailure(M07Error): retryable = True
class QualityFailure(M07Error): pass
class InvariantFailure(M07Error): pass
