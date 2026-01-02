# src/chess/coord/service/exception/catchall.py

"""
Module: chess.coord.service.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# COORD_SERVICE EXCEPTION #======================#
    "CoordServiceException",
]

from chess.coord import CoordException
from chess.system import ServiceException


# ======================# COORD_SERVICE EXCEPTION #======================#
class CoordServiceException(CoordException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an CoordService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a CoordService method.

    # PARENT:
        *   ServiceException
        *   CoordException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordService raised an exception."
