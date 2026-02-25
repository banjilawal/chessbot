# src/chess/square/validator/exception/null.py

"""
Module: chess.square.validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
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
    A failing ValidationResult was returned because the candidate was null.

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
    ERROR_CODE = "NULL_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square validation failed: The candidate cannot be null."