# src/chess/square/context/validator/exception/debug/excess.py

"""
Module: chess.square.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.square import SquareContextException

__all__ = [
    # ========================= EXCESSIVE_SQUARE_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveSquareContextFlagsException"
]


# ========================= EXCESSIVE_SQUARE_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveSquareContextFlagsException(SquareContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a SquareContext because more than one of its attributes
        was enabled.

    # PARENT:
        *   ContextFlagCountException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_SQUARE_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "SquareContext validation failed: More than one flag was enable."