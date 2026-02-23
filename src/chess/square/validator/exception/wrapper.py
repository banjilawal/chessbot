# src/chess/square/validator/exception/wrapper.py

"""
Module: chess.square.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-11-19
"""

from chess.system import ValidationException

__all__ = [
    # ======================# SQUARE_VALIDATION_FAILURE #======================#
    "SquareValidationException",
]


# ======================# SQUARE_VALIDATION_FAILURE #======================#
class SquareValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    An error occurred in SquareValidator.validate that, prevented ValidationResult.success() from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Square validation failed."
