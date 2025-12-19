# src/chess/coord/validator/exception/column/null.py

"""
Module: chess.coord.validator.exception.column.null
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import NullException
from chess.coord import InvalidCoordException

__all__ = [
    # ======================# NULL COORD EXCEPTION #======================#
    "CoordNullColumnException",
]


# ======================# COORD_NULL_COLUMN EXCEPTION #======================#
class CoordNullColumnException(InvalidCoordException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if a Coord.column field is null.

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
    ERROR_CODE = "COORD_COLUMN_NULL_ERROR"
    DEFAULT_MESSAGE = "Coord cannot have a null column."