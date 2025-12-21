# src/chess/coord/map/service/exception/exception

"""
Module: chess.coord.map.service.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.coord import CoordContext
from chess.system import ServiceException

__all__ = [
    # ======================# COORD_CONTEXT_SERVICE EXCEPTION #======================#
    "CoordContextServiceException",
]


# ======================# COORD_CONTEXT_SERVICE EXCEPTION #======================#
class CoordContextServiceException(CoordContext, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when an CoordContextService's normal operations are halted
        by an error condition.
    2.  Raised when no specific exception exists for the error interrupting CoordContextService's
        processes from their normal flows.

    # PARENT:
        *   CoordContext
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CoordContextService raised an exception."