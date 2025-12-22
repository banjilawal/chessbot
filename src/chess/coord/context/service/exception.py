# src/chess/coord/service/exception/exception

"""
Module: chess.coord.service.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.coord import CoordContext
from chess.system import ServiceException
from chess.system import ServiceException
from chess.coord import CoordContextException

__all__ = [
    # ======================# COORD_CONTEXT_SERVICE EXCEPTION #======================#
    "CoordContextServiceException",
]


# ======================# COORD_CONTEXT_SERVICE EXCEPTION #======================#
class CoordContextServiceException(CoordContextException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an CoordContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an CoordContextService method.

    # PARENT:
        *   ServiceException
        *   CoordContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordContextService raised an exception."