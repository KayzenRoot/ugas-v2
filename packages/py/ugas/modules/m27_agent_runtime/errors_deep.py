# GENERATED-DEEP-PREPROGRAMMED
class M27Error(Exception):
    retryable: bool = False

class ValidationFailure(M27Error): pass
class PolicyFailure(M27Error): pass
class CapabilityFailure(M27Error): retryable = True
class QualityFailure(M27Error): pass
class InvariantFailure(M27Error): pass
