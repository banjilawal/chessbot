# src/chess/square/service/data/unique/exception/catchall.py

"""
Module: chess.square.service.data.unique.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

___all__ = [
    # ======================# PLAYER_DATA_SERVICE EXCEPTION #======================#
    "UniqueSquareDataServiceException",
]

from chess.square import SquareException
from chess.system import UniqueDataServiceException


# ======================# UNIQUE_SQUARE_DATA_SERVICE EXCEPTION #======================#
class UniqueSquareDataServiceException(SquareException, UniqueDataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an UniqueSquareDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a UniqueSquareDataService method.

    # PARENT:
        *   ServiceException
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueSquareDataService raised an exception."