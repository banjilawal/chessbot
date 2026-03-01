# src/logic/board/database/core/super.py

"""
Module: logic.board.database.core.super
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

___all__ = [
    # ======================# BOARD_STACK_SERVICE EXCEPTION #======================#
    "BoardDataServiceException",
]

from logic.board import BoardException
from logic.system import DataServiceException


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
    ERR_CODE = "BOARD_STACK_EXCEPTION"
    MSG = "BoardStackService raised an exception."