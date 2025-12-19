# src/chess/coord/service/exception/base.py

"""
Module: chess.coord.service.exception.base
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import ServiceException

__all__ = [
    # ======================# COORD_SERVICE EXCEPTIONS #======================#
    "CoordServiceException",
]


# ======================# COORD_SERVICE EXCEPTIONS #======================#
class CoordServiceException(CoordException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by CoordService objects.
    2.  Raised when an exception hits the try-finally block of a CoordService method.
    3.  Catchall for CoordService failures that are not covered by a lower level CoordService exceptions.

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
    ERROR_CODE = "COORD_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "CoordService raised an exception."