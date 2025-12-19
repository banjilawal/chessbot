# src/chess/coord/validator/exception/column/above.py

"""
Module: chess.coord.validator.exception.column.above
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import BoundsException
from chess.coord import InvalidCoordException

__all__ = [
    # ======================# COLUMN ABOVE BOUNDS EXCEPTION #======================#
    "ColumnAboveBoundsException",
]


# ======================# COLUMN ABOVE BOUNDS EXCEPTION #======================#
class ColumnAboveBoundsException(InvalidCoordException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates a value above the height of the board is being passed a column value.

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
    ERROR_CODE = "COLUMN_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A column index cannot exceed the size of the board."