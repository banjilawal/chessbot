# src/chess/system/err/number/exception/negative.py

"""
Module: chess.system.err.number.exception.negative
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BoundsException, InvalidNumberException

__all__ = [
    # ======================# NEGATIVE NUMBER EXCEPTION #======================#
    "NegativeNumberException",
]


# ======================# NEGATIVE NUMBER EXCEPTION #======================#
class NegativeNumberException(InvalidNumberException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates a negative number was passed when a value zero or greater is required.

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
    DEFAULT_MESSAGE = (
        "Number cannot be negative. A number less than zero was received when the value "
        "must be zero or greater."
    )