# src/chess/system/identity/id/exception.py

"""
Module: chess.system.identity.id.exception
Author: Banji Lawal
Created: 2025-09-17
version: 1.0.0
"""

from chess.system import NumberException, ValidationFailedException

__all__ = [
    # ======================# ID_VALIDATION EXCEPTION #======================#
    "IdValidationFailedException",
]


# ======================# ID_VALIDATION EXCEPTION #======================#
class IdValidationFailedException(NumberException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when an ID candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an IdValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The IdValidationFailedException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   NumberException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ID_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Id Validation failed."
