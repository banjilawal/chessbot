# src/logic/coord/database/core/exception/base.py

"""
Module: logic.coord.database.core.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

___all__ = [
    # ======================# COORD_STACK EXCEPTION #======================#
    "CoordStackException",
]

from logic.coord import CoordException
from logic.system import StackServiceException


# ======================# COORD_STACK EXCEPTION #======================#
class CoordStackException(CoordException, StackServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an CoordStack encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a CoordStack method.

    # PARENT:
        *   StackServiceException
        *   CoordDataException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "COORD_STACK_EXCEPTION"
    MSG = "CoordStack raised an exception."