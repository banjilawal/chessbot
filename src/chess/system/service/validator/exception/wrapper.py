__all__ = [
    # ======================# ENTITY_SERVICE_VALIDATION_FAILURE EXCEPTION #======================#
    "EntityServiceValidationException",
]

from chess.system import ServiceException, ValidationException


# ======================# ENTITY_SERVICE_VALIDATION_FAILURE EXCEPTION #======================#
class EntityServiceValidationException(ServiceException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Service candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an EntityServiceValidationException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The EntityServiceValidationException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   ServiceException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ENTITY_SERVICE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "EntityService validation failed."