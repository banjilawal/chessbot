# src/chess/square/service/data/exception.py

"""
Module: chess.square.service.data.exception
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

___all__ = [
    # ======================# SQUARE_DATA_SERVICE EXCEPTION #======================#
    "SquareDataServiceException",
]

from chess.square import SquareException
from chess.system import ServiceException


# ======================# SQUARE_DATA_SERVICE EXCEPTION #======================#
class SquareDataServiceException(SquareException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SquareDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SquareDataService method.

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
    ERROR_CODE = "SQUARE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareDataService raised an exception."