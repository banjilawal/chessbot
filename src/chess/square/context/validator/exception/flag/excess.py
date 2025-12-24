# src/chess/square_name/validator/exception/flag/excess.py

"""
Module: chess.square_name.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.square import InvalidSquareContextException

__all__ = [
    # ========================= EXCESSIVE_SQUARE_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveSquareContextFlagsException"
]


# ========================= EXCESSIVE_SQUARE_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveSquareContextFlagsException(InvalidSquareContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one SquareContext flag was enabled. Only one Square attribute-value-tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidSquareContextException

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