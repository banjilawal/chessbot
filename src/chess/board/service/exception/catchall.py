# src/chess/board/service/exception/catchall.py

"""
Module: chess.board.service.exception.catchall
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_SERVICE EXCEPTION #======================#
    "BoardServiceException",
]

from chess.board import BoardException
from chess.system import ServiceException


# ======================# BOARD_SERVICE EXCEPTION #======================#
class BoardServiceException(BoardException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an BoardService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a BoardService method.

    # PARENT:
        *   ServiceException
        *   BoardException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SERVICE_ERROR"
    DEFAULT_MESSAGE = "BoardService raised an exception."