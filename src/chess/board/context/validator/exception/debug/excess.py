# src/chess/board/context/validator/exception/debug/excess.py

"""
Module: chess.board.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.board import BoardContextException

__all__ = [
    # ========================= EXCESSIVE_BOARD_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveBoardContextFlagsException"
]


# ========================= EXCESSIVE_BOARD_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveBoardContextFlagsException(BoardContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one BoardContext flag was enabled. Only one Board attribute-value-tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   BoardContextValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_BOARD_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = (
        "Excessive BoardContext flags were set. an Board search can only use one-and-only "
        "map flag at a time."
    )
