# src/chess/coord/validator/exception/row/above.py

"""
Module: chess.coord.validator.exception.row.above
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import BoundsException
from chess.coord import InvalidCoordException

__all__ = [
    # ======================# ROW ABOVE BOUNDS EXCEPTION #======================#
    "RowAboveBoundsException",
]


# ======================# ROW ABOVE BOUNDS EXCEPTION #======================#
class RowAboveBoundsException(InvalidCoordException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates a value above the height of the board is being passed a row value.

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
    ERROR_CODE = "ROW_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A row index cannot exceed the size of the board."