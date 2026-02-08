# src/chess/square/validator/exception/wrapper.py

"""
Module: chess.square.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-19
"""

from chess.square import SquareException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# SQUARE_VALIDATION_FAILURE EXCEPTION #======================#
    "SquareValidationFailedException",
]


# ======================# SQUARE_VALIDATION_FAILURE EXCEPTION #======================#
class SquareValidationFailedException(SquareException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Square. The exception chain traces the ultimate source of failure.

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