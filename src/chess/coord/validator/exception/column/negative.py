# src/chess/coord/number_bounds_validator/exception/column/negative.py

"""
Module: chess.coord.number_bounds_validator.exception.column.negative
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import BoundsException
from chess.coord import InvalidCoordException

__all__ = [
    # ======================# NEGATIVE COLUMN EXCEPTION #======================#
    "NegativeColumnException",
]


# ======================# NEGATIVE COLUMN EXCEPTION #======================#
class NegativeColumnException(InvalidCoordException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates if a negative value is being passed as a column value.

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
    ERROR_CODE = "NEGATIVE_COLUMN_ERROR"
    DEFAULT_MESSAGE = "A column index cannot negative."