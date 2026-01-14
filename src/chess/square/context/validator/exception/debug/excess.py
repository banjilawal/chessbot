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
    1.  Indicate That  more than one SquareContext flag was enabled. Only one Square attribute-value-tuple can be used in
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
    ERROR_CODE = "EXCESSIVE_SQUARE_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = (
        "Excessive SquareContext flags were set. an Square search can only use one-and-only "
        "map flag at a time."
    )