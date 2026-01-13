# src/chess/square/service/exception/catchall.py

"""
Module: chess.square.service.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""


from chess.system import ServiceException
from chess.square import SquareException

__all__ = [
    # ======================# SQUARE_SERVICE EXCEPTION #======================#
    "SquareServiceException",
]


# ======================# SQUARE_SERVICE EXCEPTION #======================#
class SquareServiceException(SquareException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SquareService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SquareService method.

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
    ERROR_CODE = "SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareService raised an exception."