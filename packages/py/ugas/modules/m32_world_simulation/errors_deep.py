# GENERATED-DEEP-PREPROGRAMMED
class M32Error(Exception):
    retryable: bool = False

class ValidationFailure(M32Error): pass
class PolicyFailure(M32Error): pass
class CapabilityFailure(M32Error): retryable = True
class QualityFailure(M32Error): pass
class InvariantFailure(M32Error): pass
