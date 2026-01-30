# src/chess/square/database/core/catchall.py

"""
Module: chess.square.database.core.catchall
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

___all__ = [
    # ======================# SQUARE_STACK EXCEPTION #======================#
    "SquareStackServiceException",
]

from chess.square import SquareException
from chess.system import StackServiceException


# ======================# SQUARE_STACK EXCEPTION #======================#
class SquareStackServiceException(SquareException, StackServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by SquareStackService methods that return Result objects.

    # PARENT:
        *   SquareException
        *   StackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_STACK_ERROR"
    DEFAULT_MESSAGE = "SquareStackService raised an exception."