# GENERATED-DEEP-PREPROGRAMMED
class M05Error(Exception):
    retryable: bool = False

class ValidationFailure(M05Error): pass
class PolicyFailure(M05Error): pass
class CapabilityFailure(M05Error): retryable = True
class QualityFailure(M05Error): pass
class InvariantFailure(M05Error): pass
