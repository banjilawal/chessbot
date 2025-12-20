# src/chess/board/context/validator/exception/flag/zero.py

"""
Module: chess.board.context.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from chess.system import BoundsException
from chess.board import InvalidBoardContextException

__all__ = [
    # ========================= ZERO_BOARD_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroBoardContextFlagsException"
]


# ========================= ZERO_BOARD_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroBoardContextFlagsException(InvalidBoardContextException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates no BoardContext flag was enabled. One and only one Board attribute-value tuple is required for
        a search.

    # PARENT:
        *   BoundsException
        *   InvalidBoardContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_BOARD_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "Zero BoardContext flags were set. One and only one context flag must be enabled,"
