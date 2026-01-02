# src/chess/coord/service/data/exception/base.py

"""
Module: chess.coord.service.data.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

___all__ = [
    # ======================# COORD_DATA_SERVICE EXCEPTION #======================#
    "CoordDataServiceException",
]

from chess.coord import CoordException
from chess.system import ServiceException


# ======================# COORD_DATA_SERVICE EXCEPTION #======================#
class CoordDataServiceException(CoordException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an CoordDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a CoordDataService method.

    # PARENT:
        *   ServiceException
        *   CoordDataException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordDataService raised an exception."