# src/chess/board/exception/debug.py

"""
Module: chess.board.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# BOARD_DEBUG EXCEPTION #======================#
    "BoardDebugException",
]

from chess.board import BoardException
from chess.system import DebugException


# ======================# BOARD_DEBUG EXCEPTION #======================#
class BoardDebugException(BoardException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Board operation failure.

    # PARENT:
        *   BoardException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "BOARD_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A BoardDebugException was raised."