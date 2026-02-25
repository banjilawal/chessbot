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
    # ======================# SQUARE_CONTEXT_VALIDATION_FAILURE #======================#
    "SquareContextValidationException",
]


# ======================# SQUARE_CONTEXT_VALIDATION_FAILURE #======================#
class SquareContextValidationException(SquareContextException, ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    An error occurred in SquareContextValidator.validate that, prevented A successful validation result
    from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "SquareContext validation failed."