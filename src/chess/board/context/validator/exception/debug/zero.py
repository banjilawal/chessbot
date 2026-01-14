# src/chess/board/context/validator/exception/debug/zero.py

"""
Module: chess.board.context.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.board import BoardContextException

__all__ = [
    # ========================= ZERO_BOARD_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroBoardContextFlagsException"
]


# ========================= ZERO_BOARD_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroBoardContextFlagsException(BoardContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  no BoardContext flag was enabled. One and only one Board attribute-value-tuple is required for
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   BoardContextValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_BOARD_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "Zero BoardContext flags were set. Cannot search for Boards if one-and_oly-one "
        "map flag is enabled."
    )
