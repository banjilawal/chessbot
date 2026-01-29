# src/chess/board/service/data/unique/exception/catchall.py

"""
Module: chess.board.service.data.unique.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

___all__ = [
    # ======================# PLAYER_DATA_SERVICE EXCEPTION #======================#
    "UniqueBoardDataServiceException",
]

from chess.board import BoardException
from chess.system import DatabaseException


# ======================# UNIQUE_BOARD_DATA_SERVICE EXCEPTION #======================#
class UniqueBoardDataServiceException(BoardException, DatabaseException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an UniqueBoardDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a UniqueBoardDataService method.

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
    ERROR_CODE = "DATABASE_ERROR"
    DEFAULT_MESSAGE = "UniqueBoardDataService raised an exception."