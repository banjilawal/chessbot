# src/chess/system/number/exception/bounds.py

"""
Module: chess.system.number.exception.bounds
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BoundsException, InvalidNumberException

__all__ = [
    # ======================# NUMBER ABOVE BOUNDS EXCEPTION #======================#
    "NumberAboveBoundsException",
]


# ======================# NUMBER ABOVE BOUNDS EXCEPTION #======================#
class NumberAboveBoundsException(InvalidNumberException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  a value being passed a Coord or Vector component is larger than the Board's dimension.

    # PARENT:
        *   InvalidNumberException
        *   BoundsException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NUMBER_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A number index cannot exceed the size of the board."