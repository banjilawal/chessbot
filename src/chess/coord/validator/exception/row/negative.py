# src/chess/coord/validator/exception/row/negative.py

"""
Module: chess.coord.validator.exception.row.negative
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import BoundsException
from chess.coord import InvalidCoordException

__all__ = [
    # ======================# NEGATIVE ROW EXCEPTION #======================#
    "NegativeRowException",
]


# ======================# NEGATIVE ROW EXCEPTION #======================#
class NegativeRowException(InvalidCoordException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates if a zeroth or negative value is being passed as a row value.

    # PARENT:
        *   InvalidCoordException
        *   BoundsException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NEGATIVE_ROW_ERROR"
    DEFAULT_MESSAGE = "A row index cannot be less than one."