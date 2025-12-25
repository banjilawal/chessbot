# src/chess/system/number/exception/debug/above.py

"""
Module: chess.system.number.exception.debug.above
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NUMBER_ABOVE_CEILING EXCEPTION #======================#
    "NumberAboveCeilingException",
]

from chess.system import BoundsException, InvalidNumberException


# ======================# NUMBER_ABOVE_CEILING EXCEPTION #======================#
class NumberAboveCeilingException(InvalidNumberException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that number validation failed because the candidate was larger than the Board.DIMENSION.

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
    ERROR_CODE = "NUMBER_ABOVE_CEILING_ERROR"
    DEFAULT_MESSAGE = "Number validation failed: The candidate was above the ceiling."