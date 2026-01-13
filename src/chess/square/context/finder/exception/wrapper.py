# src/chess/square/context/finder/exception/wrapper.py

"""
Module: chess.square.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import SearchFailedException

__all__ = [
    # ======================# SQUARE_FINDER EXCEPTION #======================#
    "SquareSearchFailedException",
]


# ======================# SQUARE_FINDER EXCEPTION #======================#
class SquareSearchFailedException(SquareException, SearchFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when SquareFinder objects.
    2.  Wraps an exception that hits the try-finally block of an SquareFinder method.

    # PARENT:
        *   SquareException
        *   SearchFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_FINDER_ERROR"
    DEFAULT_MESSAGE = "SquareFinder raised an exception."
