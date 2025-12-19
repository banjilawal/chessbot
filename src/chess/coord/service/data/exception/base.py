# src/chess/coord/service/data/exception/base.py

"""
Module: chess.coord.service.data.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import DataServiceException

__all__ = [
    # ======================# COORD_DATA_SERVICE EXCEPTION #======================#
    "CoordDataServiceException",
]


# ======================# COORD_DATA_SERVICE EXCEPTION #======================#
class CoordDataServiceException(CoordException, DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by CoordDataService objects.
    2.  Raised when an exception hits the try-finally block of a CoordDataService method.
    3.  Catchall for CoordDataService failures that are not covered by a lower level CoordDataService exceptions.

    # PARENT:
        *   CoordException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_DATA_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "CoordDataService raised an exception."