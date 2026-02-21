# src/chess/square/context/validator/exception/wrapper.py

"""
Module: chess.square.context.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ValidationException
from chess.square import SquareContextException

__all__ = [
    # ======================# SQUARE_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "SquareContextValidationException",
]


# ======================# SQUARE_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class SquareContextValidationException(SquareContextException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a SquareContext. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   SquareContextException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "SquareContext validation failed."