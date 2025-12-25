__all__ = [
    # ======================# SERVICE_VALIDATION_FAILURE EXCEPTION #======================#
    "ServiceValidationFailedException",
]

from chess.system import ServiceException, ValidationFailedException


# ======================# SERVICE_VALIDATION_FAILURE EXCEPTION #======================#
class ServiceValidationFailedException(ServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Service candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an ServiceValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The ServiceValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   ServiceException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SERVICE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Service validation failed."