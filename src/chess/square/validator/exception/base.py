# src/chess/square/validator/exception/base_.py

"""
Module: chess.square.validator.exception.base_
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
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicates a Square validation candidate failed a verification test.
    2.  Wraps unhandled exceptions that hit the finally-block in SquareValidator methods.

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