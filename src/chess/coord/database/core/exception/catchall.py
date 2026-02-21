# src/chess/coord/database/core/exception/base.py

"""
Module: chess.coord.database.core.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

___all__ = [
    # ======================# COORD_STACK EXCEPTION #======================#
    "CoordStackException",
]

from chess.coord import CoordException
from chess.system import StackException


# ======================# COORD_STACK EXCEPTION #======================#
class CoordStackException(CoordException, StackException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an CoordStack encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a CoordStack method.

    # PARENT:
        *   StackException
        *   CoordDataException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_STACK_ERROR"
    DEFAULT_MESSAGE = "CoordStack raised an exception."