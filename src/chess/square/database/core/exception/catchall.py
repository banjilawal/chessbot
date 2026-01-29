# src/chess/square/database/core/catchall.py

"""
Module: chess.square.database.core.catchall
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

___all__ = [
    # ======================# SQUARE_DATA_SERVICE EXCEPTION #======================#
    "SquareDataServiceException",
]

from chess.square import SquareException
from chess.system import DataServiceException


# ======================# SQUARE_DATA_SERVICE EXCEPTION #======================#
class SquareDataServiceException(SquareException, DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by SquareListService methods that return Result objects.

    # PARENT:
        *   SquareException
        *   DataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareListService raised an exception."