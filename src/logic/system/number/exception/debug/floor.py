# src/logic/system/number/exception/debug/above.py

"""
Module: logic.system.number.exception.debug.above
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NUMBER_BELOW_FLOOR EXCEPTION #======================#
    "NumberBelowFloorException",
]

from logic.system import BoundsException, NumberException


# ======================# NUMBER_BELOW_FLOOR EXCEPTION #======================#
class NumberBelowFloorException(NumberException, BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that number validation failed because the rank was smaller than the floor.

    Super Class:
        *   NumberException
        *   BoundsException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NUMBER_BELOW_FLOOR_EXCEPTION"
    MSG = "Number validation failed: The rank was below the floor."