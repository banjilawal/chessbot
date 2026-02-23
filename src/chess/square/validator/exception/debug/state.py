# src/chess/square/validator/exception/null.py

"""
Module: chess.square.validator.exception.null
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# NULL_SQUARE_STATE EXCEPTION #======================#
    "NullSquareStateException",
]

from chess.system import DebugException, NullException

# ======================# NULL_SQUARE_STATE EXCEPTION #======================#
class NullSquareStateException(DebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failure ValidationResult was returned because the validation candidate was null instead of
        being a SquareState.

    # PARENT:
        *   DebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SQUARE_STATE"
    DEFAULT_MESSAGE = "SquareState validation failed: The validation candidate cannot be null."