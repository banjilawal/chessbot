# src/chess/system/number/exception/debug/negative.py

"""
Module: chess.system.number.exception.debug.negative
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BoundsException, InvalidNumberException

__all__ = [
    # ======================# NEGATIVE_NUMBER EXCEPTION #======================#
    "NegativeNumberException",
]


# ======================# NEGATIVE_NUMBER EXCEPTION #======================#
class NegativeNumberException(InvalidNumberException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that number validation failed because the candidate was negative.

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
    ERROR_CODE = "NEGATIVE_NUMBER_ERROR"
    DEFAULT_MESSAGE = "Number validation failed: The candidate was negative."