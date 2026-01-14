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
    1.  Indicate That  no SquareContext flag was enabled. One and only one Square attribute-value-tuple is required for
        a search.

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
    DEFAULT_MESSAGE = (
        "Zero SquareContext flags were set. Cannot search for Squares if one-and_oly-one "
        "map flag is enabled."
    )