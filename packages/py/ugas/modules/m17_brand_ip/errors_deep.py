# GENERATED-DEEP-PREPROGRAMMED
class M17Error(Exception):
    retryable: bool = False

class ValidationFailure(M17Error): pass
class PolicyFailure(M17Error): pass
class CapabilityFailure(M17Error): retryable = True
class QualityFailure(M17Error): pass
class InvariantFailure(M17Error): pass
