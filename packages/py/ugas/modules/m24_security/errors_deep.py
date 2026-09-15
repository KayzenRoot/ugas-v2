# GENERATED-DEEP-PREPROGRAMMED
class M24Error(Exception):
    retryable: bool = False

class ValidationFailure(M24Error): pass
class PolicyFailure(M24Error): pass
class CapabilityFailure(M24Error): retryable = True
class QualityFailure(M24Error): pass
class InvariantFailure(M24Error): pass
