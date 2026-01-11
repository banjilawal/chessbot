# src/board/searcher/exception.py

"""
Module: chess.board.searcher.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


__all__ = [
    # ======================# NULL_BOARD_CONTEXT EXCEPTION #======================#
    "NullBoardContextException",
]

from chess.system import NullException
from chess.board import BoardContextException


# ======================# NULL_BOARD_CONTEXT EXCEPTION #======================#
class NullBoardContextException(BoardContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that BoardContext validation failed because the candidate was null.

    # PARENT:
        *   NullBoardContextException
        *   InvalidBoardContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_BOARD_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "BoardContext validation failed: The candidate was null."