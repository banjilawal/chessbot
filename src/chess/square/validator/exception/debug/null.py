# src/chess/square/validator/exception/null.py

"""
Module: chess.square.validator.exception.null
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# NULL_SQUARE EXCEPTION #======================#
    "NullSquareException",
]

from chess.system import NullException
from chess.square import SquareDebugException

# ======================# NULL_SQUARE EXCEPTION #======================#
class NullSquareException(SquareDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failure ValidationResult was returned because the validation candidate was null.

    # PARENT:
        *   SquareDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_NOT_REGISTERED_WITH_BOARD_ERROR"
    DEFAULT_MESSAGE = "Square validation failed: The validation candidate cannot be null"