# src/chess/board/context/finder/exception/wrapper.py

"""
Module: chess.board.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.board import BoardException
from chess.system import SearchFailedException

__all__ = [
    # ======================# BOARD_FINDER EXCEPTION #======================#
    "BoardSearchFailedException",
]


# ======================# BOARD_FINDER EXCEPTION #======================#
class BoardSearchFailedException(BoardException, SearchFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when BoardFinder objects.
    2.  Wraps an exception that hits the try-finally block of an BoardFinder method.

    # PARENT:
        *   BoardException
        *   SearchFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_FINDER_ERROR"
    DEFAULT_MESSAGE = "BoardFinder raised an exception."