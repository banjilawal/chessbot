# src/logic/system/number/exception/debug/above.py

"""
Module: logic.system.number.exception.debug.above
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NUMBER_ABOVE_CEILING EXCEPTION #======================#
    "NumberAboveCeilingException",
]

from system import BoundsException, NumberException


# ======================# NUMBER_ABOVE_CEILING EXCEPTION #======================#
class NumberAboveCeilingException(NumberException, BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that number validation failed because the rank was larger than the Board.DIMENSION.

    Super Class:
        *   NumberException
        *   BoundsException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NUMBER_ABOVE_CEILING_EXCEPTION"
    MSG = "Number validation failed: The rank was above the ceiling."