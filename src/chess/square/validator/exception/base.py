# src/chess/square/validator/exception/base.py

"""
Module: chess.square.validator.exception.base
Author: Banji Lawal
Created: 2025-11-19
"""

from chess.square import SquareException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# SQUARE_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidSquareException",
]


# ======================# SQUARE_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidSquareException(SquareException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Square candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidSquareException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidSquareException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   SquareException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Square validation failed."