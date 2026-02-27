# src/chess/square/context/validator/exception/debug/excess.py

"""
Module: chess.square.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.square import SquareContextDebugException

__all__ = [
    # ========================= EXCESS_SQUARE_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessSquareContextFlagsException"
]


# ========================= EXCESS_SQUARE_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessSquareContextFlagsException(SquareContextDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

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
    ERR_CODE = "EXCESS_SQUARE_CONTEXT_FLAGS_EXCEPTION"
    MSG = "SquareContext validation failed: More than one flag was enable."