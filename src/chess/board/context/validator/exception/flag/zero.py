# src/chess/board/map/validator/exception/flag/zero.py

"""
Module: chess.board.map.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.board import InvalidBoardContextException

__all__ = [
    # ========================= ZERO_BOARD_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroBoardContextFlagsException"
]


# ========================= ZERO_BOARD_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroBoardContextFlagsException(InvalidBoardContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates no BoardContext flag was enabled. One and only one Board attribute-value-tuple is required for
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
    ERROR_CODE = "ZERO_BOARD_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "Zero BoardContext flags were set. Cannot search for Boards if one-and_oly-one "
        "map flag is enabled."
    )
