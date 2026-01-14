# src/chess/square/context.validator/exception/wrapper.py

"""
Module: chess.square.context.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.square import SquareContextException

__all__ = [
    # ======================# SQUARE_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "SquareContextValidationFailedException",
]


# ======================# SQUARE_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class SquareContextValidationFailedException(SquareContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a SquareContext. The encapsulated
        exceptions create a chain for tracing the source of the failure.

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