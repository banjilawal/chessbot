# src/chess/coord/database/exception/catchall.py

"""
Module: chess.coord.database.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import DatabaseException

__all__ = [
    # ======================# COORD_DATABASE EXCEPTION #======================#
    "CoordDatabaseException",
]


# ======================# COORD_DATABASE EXCEPTION #======================#
class CoordDatabaseException(CoordException, DatabaseException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by CoordDatabase objects.
    2.  Raised when an exception hits the try-finally block of a CoordDatabase method.
    3.  Catchall for CoordDatabase failures that are not covered by a lower level CoordDatabase exceptions.

    # PARENT:
        *   CoordException
        *   DatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_DATABASE_ERROR"
    DEFAULT_ERROR_CODE = "CoordDatabase raised an exception."