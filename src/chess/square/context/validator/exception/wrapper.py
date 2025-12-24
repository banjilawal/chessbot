# src/chess/square/validator/exception/exception.py

"""
Module: chess.square.validator.exception.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ValidationException, ValidationFailedException
from chess.square import SquareContextException

__all__ = [
    # ======================# SQUARE_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidSquareContextException",
]


# ======================# SQUARE_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidSquareContextException(SquareContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a SquareContext candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidSquareContextException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidSquareContextException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   SquareContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "SquareContext validation failed."