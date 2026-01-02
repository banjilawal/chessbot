# src/chess/coord/service/data/unique/exception/base.py

"""
Module: chess.coord.service.data.unique.exception.base
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import DataServiceException

__all__ = [
    # ======================# UNIQUE_COORD_DATA_SERVICE EXCEPTION #======================#
    "UniqueCoordDataServiceException",
]


# ======================# UNIQUE_COORD_DATA_SERVICE EXCEPTION #======================#
class UniqueCoordDataServiceException(CoordException, DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by UniqueCoordDataService objects.
    2.  Raised when an exception hits the try-finally block of a UniqueCoordDataService method.
    3.  Catchall for UniqueCoordDataService failures that are not covered by a lower level UniqueCoordDataService exceptions.

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
    ERROR_CODE = "UNIQUE_COORD_DATA_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "UniqueCoordDataService raised an exception."