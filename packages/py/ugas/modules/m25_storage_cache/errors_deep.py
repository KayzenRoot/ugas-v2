# GENERATED-DEEP-PREPROGRAMMED
class M25Error(Exception):
    retryable: bool = False

class ValidationFailure(M25Error): pass
class PolicyFailure(M25Error): pass
class CapabilityFailure(M25Error): retryable = True
class QualityFailure(M25Error): pass
class InvariantFailure(M25Error): pass
