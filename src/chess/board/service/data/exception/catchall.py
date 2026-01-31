# src/chess/board/database/core/catchall.py

"""
Module: chess.board.database.core.catchall
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

___all__ = [
    # ======================# BOARD_STACK_SERVICE EXCEPTION #======================#
    "BoardDataServiceException",
]

from chess.board import BoardException
from chess.system import DataServiceException


# ======================# BOARD_STACK_SERVICE EXCEPTION #======================#
class BoardDataServiceException(BoardException, DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by BoardStackService methods that return Result objects.

    # PARENT:
        *   BoardException
        *   StackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_DATABASE_CORE_ERROR"
    DEFAULT_MESSAGE = "BoardStackService raised an exception."