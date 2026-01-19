# src/chess/square/context/validator/exception/debug/zero.py

"""
Module: chess.square.context.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.square import SquareContextException

__all__ = [
    # ========================= ZERO_SQUARE_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroSquareContextFlagsException"
]


# ========================= ZERO_SQUARE_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroSquareContextFlagsException(SquareContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its validation as a SquareContext because none of its attributes was enabled.
        A single SquareContext attribute.

    # PARENT:
        *   ContextFlagCountException
        *   SquareContextValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_SQUARE_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "SquareContext validation failed: None of the flags were set. A single flag must be enabled."