# src/logic/system/number/exception/debug/negative.py

"""
Module: logic.system.number.exception.debug.negative
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from system import BoundsException, NumberException

__all__ = [
    # ======================# NOT_NEGATIVE_NUMBER_VALIDATION_FAILURE #======================#
    "NegativeNumberNotAllowedException",
]


# ======================# NOT_NEGATIVE_NUMBER_VALIDATION_FAILURE #======================#
class NegativeNumberNotAllowedException(NumberException, BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that number validation failed because the rank was negative.

    Super Class:
        *   NumberException
        *   BoundsException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NOT_NEGATIVE_NUMBER_VALIDATION_FAILURE"
    MSG = "Number validation failed: The rank was negative."