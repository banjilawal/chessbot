# src/chess/system/number/exception/invalid.py

"""
Module: chess.system.number.exception.invalid
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NUMBER_VALIDATION_FAILURE EXCEPTION #======================#
    "NumberValidationFailedException",
]

from chess.system import NumberException, ValidationFailedException


# ======================# NUMBER_VALIDATION_FAILURE EXCEPTION #======================#
class NumberValidationFailedException(NumberException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Number candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an NumberValidationFailedException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The NumberValidationFailedException chain is useful for tracing a  failure to its source.

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
    ERROR_CODE = "NUMBER_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Number validation failed."