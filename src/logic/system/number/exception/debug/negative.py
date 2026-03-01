# src/logic/system/number/exception/debug/negative.py

"""
Module: logic.system.number.exception.debug.negative
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import BoundsException, NumberException

__all__ = [
    # ======================# NOT_NEGATIVE_NUMBER_VALIDATION_FAILURE #======================#
    "NegativeNumberNotAllowedException",
]


# ======================# NOT_NEGATIVE_NUMBER_VALIDATION_FAILURE #======================#
class NegativeNumberNotAllowedException(NumberException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that number validation failed because the candidate was negative.

    # PARENT:
        *   NumberException
        *   BoundsException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NOT_NEGATIVE_NUMBER_VALIDATION_FAILURE"
    MSG = "Number validation failed: The candidate was negative."