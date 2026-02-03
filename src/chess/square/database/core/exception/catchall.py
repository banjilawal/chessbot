# src/chess/square/database/core/catchall.py

"""
Module: chess.square.database.core.catchall
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

___all__ = [
    # ======================# SQUARE_STACK EXCEPTION #======================#
    "SquareStackException",
]

from chess.square import SquareException
from chess.system import StackException


# ======================# SQUARE_STACK EXCEPTION #======================#
class SquareStackException(SquareException, StackException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wrap any exceptions raised by SquareStack methods that return Result objects.

    # PARENT:
        *   SquareException
        *   StackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_STACK_ERROR"
    DEFAULT_MESSAGE = "SquareStack raised an exception."