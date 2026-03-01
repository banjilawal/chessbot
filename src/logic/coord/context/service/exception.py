# src/logic/coord/context/service/exception.py

"""
Module: logic.coord.context.service.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from logic.coord import CoordContext
from logic.system import ServiceException
from logic.system import ServiceException
from logic.coord import CoordContextException

__all__ = [
    # ======================# COORD_CONTEXT_SERVICE EXCEPTION #======================#
    "CoordContextServiceException",
]


# ======================# COORD_CONTEXT_SERVICE EXCEPTION #======================#
class CoordContextServiceException(CoordContextException, ServiceException):
    """
    # ROLE: Exception Wrapper

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
    ERR_CODE = "COORD_CONTEXT_SERVICE_EXCEPTION"
    MSG = "CoordContextService raised an exception."