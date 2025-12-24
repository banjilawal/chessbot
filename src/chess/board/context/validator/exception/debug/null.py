# src/board/searcher/exception.py

"""
Module: chess.board.searcher.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import NullException
from chess.board import InvalidBoardContextException

__all__ = [
    # ======================# NULL_BOARD_CONTEXT EXCEPTION #======================#
    "NullBoardContextException",
]




# ======================# NULL_BOARD_CONTEXT EXCEPTION #======================#
class NullBoardContextException(InvalidBoardContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a BoardContext validation candidate is null.
    2.  Raised if an entity, method or operation requires a BoardContext but receives null instead.

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
    ERROR_CODE = "NULL_BOARD_CONTEXT__ERROR"
    DEFAULT_MESSAGE = "BoardContext cannot be null."