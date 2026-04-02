# src/logic/board/context/service/exception.py

"""
Module: logic.board.context.service.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from logic.system import ServiceException
from logic.board import BoardContextException

__all__ = [
    # ======================# BOARD_CONTEXT_SERVICE EXCEPTION #======================#
    "BoardContextServiceException",
]


# ======================# BOARD_CONTEXT_SERVICE EXCEPTION #======================#
class BoardContextServiceException(BoardContextException, ServiceException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Indicate that an BoardQueryService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an BoardQueryService method.

    Super Class:
        *   ServiceException
        *   BoardContextException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_CONTEXT_SERVICE_EXCEPTION"
    MSG = "BoardQueryService raised an exception."