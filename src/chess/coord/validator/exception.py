# src/chess/coord/validator/exception_.py

"""
Module: chess.coord.validator.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordException
from chess.system import  NullException, ValidationException

__all__ = [
    "InvalidCoordException",
    
    # ====================== COORD_ROW VALIDATION EXCEPTIONS #======================#
    "NullRowException",
    "RowBelowBoundsException",
    "RowAboveBoundsException",
    
    # ====================== COORD_COLUMN VALIDATION EXCEPTIONS #======================#
    "NullColumnException",
    "ColumnAboveBoundsException",
    "ColumnBelowBoundsException",
]


# ====================== COORD VALIDATION EXCEPTIONS #======================#
class InvalidCoordException(CoordException, ValidationException):
    """Catchall Exception for CoordValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "COORD_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Coord validation failed."


# ====================== COORD_ROW VALIDATION EXCEPTIONS #======================#
class NullRowException(CoordException, NullException):
    """Raised if Coord.row is null."""
    ERROR_CODE = "NULL_COORD_ROW_ERROR"
    DEFAULT_MESSAGE = "Coord.row property cannot be null."


class RowBelowBoundsException(InvalidCoordException):
    """Raised if trying to access row.index < 0."""
    ERROR_CODE = "COORD_ROW_INDEX_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coord.row < 0. This outside the dimension of the board."


class RowAboveBoundsException(InvalidCoordException):
    """Raised if trying to access row above array dimension."""
    ERROR_CODE = "COORD_ROW_INDEX_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coord.row > (ROW_SIZE-1). This outside the dimension of the board."


# ====================== COORD_COLUMN VALIDATION EXCEPTIONS #======================#
class NullColumnException(InvalidCoordException, NullException):
    """Raised if Coord.row is null."""
    ERROR_CODE = "NULL_COORD_COLUMN_INDEX_ERROR"
    DEFAULT_MESSAGE = "Coord.column property cannot be null."


class ColumnBelowBoundsException(InvalidCoordException):
    """Raised if trying to access column.index < 0."""
    ERROR_CODE = "COORD_COLUMN_INDEX_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coordinate.column < 0. This outside the dimension of the board."


class ColumnAboveBoundsException(InvalidCoordException):
    """Raised if trying to access column above array dimension."""
    ERROR_CODE = "COLUMN_ABOVE_INDEX_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coord.column > (COLUMN_SIZE-1). This outside the dimension of the board."
