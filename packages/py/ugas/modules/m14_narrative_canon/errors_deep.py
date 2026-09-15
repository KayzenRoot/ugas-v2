# GENERATED-DEEP-PREPROGRAMMED
class M14Error(Exception):
    retryable: bool = False

class ValidationFailure(M14Error): pass
class PolicyFailure(M14Error): pass
class CapabilityFailure(M14Error): retryable = True
class QualityFailure(M14Error): pass
class InvariantFailure(M14Error): pass
