# src/chess/square/validator/exception/wrapper.py

"""
Module: chess.square.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-19
"""

from chess.square import SquareException
from chess.system import ValidationException

__all__ = [
    # ======================# SQUARE_VALIDATION_FAILURE #======================#
    "SquareValidationException",
]


# ======================# SQUARE_VALIDATION_FAILURE #======================#
class SquareValidationException(SquareException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Square. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   SquareException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Square validation failed."