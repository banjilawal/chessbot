# src/chess/board/context/validator/exception/debug/null.py

"""
Module: chess.board.context.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import NullException
from chess.board import BoardContextException

__all__ = [
    # ======================# NULL_BOARD_CONTEXT EXCEPTION #======================#
    "NullBoardContextException",
]


# ======================# NULL_BOARD_CONTEXT EXCEPTION #======================#
class NullBoardContextException(BoardContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that BoardContext validation failed because the candidate was null.

    # PARENT:
        *   BoardContextException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_BOARD_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "BoardContext validation failed: The candidate was null."