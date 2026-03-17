# src/logic/system/number/exception/debug/null.py

"""
Module: logic.system.number.exception.debug.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import NumberException, NullException

__all__ = [
    # ======================# NULL_NUMBER EXCEPTION #======================#
    "NullNumberException",
]


# ======================# NULL_NUMBER EXCEPTION #======================#
class NullNumberException(NumberException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that number validation failed because the candidate was null.

    Super Class:
        *   NumberException
        *   NullNumberException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_NUMBER_EXCEPTION"
    MSG = "Number validation failed: The candidate was null."