# src/chess/square/context/validator/exception/debug/excess.py

"""
Module: chess.square.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.square import SquareContextDebugException

__all__ = [
    # ========================= EXCESSIVE_SQUARE_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessiveSquareContextFlagsException"
]


# ========================= EXCESSIVE_SQUARE_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessiveSquareContextFlagsException(SquareContextDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because the candidate square_context had more than one Square
        attribute switched on.

    # PARENT:
        *   SquareContextDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_SQUARE_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "SquareContext validation failed: More than one flag was enable."