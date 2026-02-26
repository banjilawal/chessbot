# src/chess/board/context/exception.py

"""
Module: chess.board.context.exception
Author: Banji Lawal
Created: 2025-11-24
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
    # ROLE: Super Exception

    # RESPONSIBILITIES:
    1.  Super for BoardContext errors not covered by BoardException subclasses.

    # PARENT:
        *   BoardException
        *   ContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_CONTEXT_ERROR"
    MSG = "BoardContext raised an exception."

