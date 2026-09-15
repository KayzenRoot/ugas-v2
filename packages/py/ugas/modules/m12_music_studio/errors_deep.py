# GENERATED-DEEP-PREPROGRAMMED
class M12Error(Exception):
    retryable: bool = False

class ValidationFailure(M12Error): pass
class PolicyFailure(M12Error): pass
class CapabilityFailure(M12Error): retryable = True
class QualityFailure(M12Error): pass
class InvariantFailure(M12Error): pass
