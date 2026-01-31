# src/chess/coord/database/core/exception/base.py

"""
Module: chess.coord.database.core.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

___all__ = [
    # ======================# COORD_STACK_SERVICE EXCEPTION #======================#
    "CoordDataServiceException",
]

from chess.coord import CoordException
from chess.system import ServiceException


# ======================# COORD_STACK_SERVICE EXCEPTION #======================#
class CoordDataServiceException(CoordException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an CoordStackService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a CoordStackService method.

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
    ERROR_CODE = "COORD_DATABASE_CORE_ERROR"
    DEFAULT_MESSAGE = "CoordStackService raised an exception."