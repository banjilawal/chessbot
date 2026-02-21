# src/chess/square/database/exception/catchall.py

"""
Module: chess.square.database.exception.catchall
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

___all__ = [
    # ======================# UNIQUE_SQUARE_STACK_SERVICE EXCEPTION #======================#
    "SquareDatabaseException",
]

from chess.square import SquareException
from chess.system import DatabaseException

# ======================# UNIQUE_SQUARE_STACK_SERVICE EXCEPTION #======================#
class SquareDatabaseException(SquareException, DatabaseException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an SquareDatabase encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SquareDatabase method.

    # PARENT:
        *   ServiceException
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_SQUARE_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareDatabase raised an exception."