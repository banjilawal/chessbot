# src/chess/board/database/core/super.py

"""
Module: chess.board.database.core.super
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
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by BoardStackService methods that return Result objects.

    # PARENT:
        *   BoardException
        *   StackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_STACK_ERROR"
    MSG = "BoardStackService raised an exception."