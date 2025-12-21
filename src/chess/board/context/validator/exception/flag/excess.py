# src/chess/board/context/validator/exception/flag/excess.py

"""
Module: chess.board.context.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.board import InvalidBoardContextException

__all__ = [
    # ========================= EXCESSIVE_BOARD_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveBoardContextFlagsException"
]


# ========================= EXCESSIVE_BOARD_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveBoardContextFlagsException(InvalidBoardContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates more than one BoardContext flag was enabled. Only one Board attribute-value-tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidBoardContextException

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
        "context flag at a time."
    )
