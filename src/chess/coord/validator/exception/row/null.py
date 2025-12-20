# src/chess/coord/number_bounds_validator/exception/row/null.py

"""
Module: chess.coord.number_bounds_validator.exception.row.null
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import NullException
from chess.coord import InvalidCoordException

__all__ = [
    # ======================# NULL COORD EXCEPTION #======================#
    "CoordNullRowException",
]


# ======================# COORD_NULL_ROW EXCEPTION #======================#
class CoordNullRowException(InvalidCoordException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a Coord.row field is null.

    # PARENT:
        *   InvalidCoordException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_ROW_NULL_ERROR"
    DEFAULT_MESSAGE = "Coord cannot have a null row."