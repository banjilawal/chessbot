# src/chess/square/validator/exception/square.py

"""
Module: chess.square.validator.exception.square
Author: Banji Lawal
Created: 2025-11-19
"""

__all__ = [
    # ======================# SQUARE_SQUARE_STATE EXCEPTION #======================#
    "SquareSquareStateException",
]

from chess.system import DebugException, SquareException

# ======================# SQUARE_SQUARE_STATE EXCEPTION #======================#
class SquareSquareStateException(DebugException, SquareException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failure ValidationResult was returned because the validation candidate was square instead of
        being a SquareState.

    # PARENT:
        *   DebugException
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_SQUARE_STATE"
    MSG = "SquareState validation failed: The candidate cannot be square."