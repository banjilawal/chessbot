# src/chess/board/context/exception.py

"""
Module: chess.game.board.context.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.board import BoardException
from chess.system import ContextException

__all__ = [
    # ======================# BOARD_CONTEXT EXCEPTION #======================#
    "BoardContextException",
]


# ======================# BOARD_CONTEXT EXCEPTION #======================#
class BoardContextException(BoardException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by BoardContext objects.
    2.  Catchall for conditions which are not covered by lower level BoardContext exceptions.

    # PARENT:
        *   BoardException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "BoardContext raised an exception."

