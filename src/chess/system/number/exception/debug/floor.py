# src/chess/system/number/exception/debug/above.py

"""
Module: chess.system.number.exception.debug.above
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NUMBER_BELOW_FLOOR EXCEPTION #======================#
    "NumberBelowFloorException",
]

from chess.system import BoundsException, InvalidNumberException


# ======================# NUMBER_BELOW_FLOOR EXCEPTION #======================#
class NumberBelowFloorException(InvalidNumberException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that number validation failed because the candidate was smaller than the floor.

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
    ERROR_CODE = "NUMBER_BELOW_FLOOR_ERROR"
    DEFAULT_MESSAGE = "Number validation failed: The candidate was below the floor."