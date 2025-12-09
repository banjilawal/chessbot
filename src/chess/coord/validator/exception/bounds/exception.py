# src/chess/coord/validator/exception/bounds/exception.py

"""
Module: chess.coord.validator.exception.bounds.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""


from chess.system import BoundsException
from chess.coord import InvalidCoordException


__all__ = [
    "RowBelowBoundsException",
    "RowAboveBoundsException",
    "ColumnBelowBoundsException",
    "ColumnAboveBoundsException",
]

#====================== COORD_ROW BOUNDS EXCEPTIONS #======================#
class RowBelowBoundsException(InvalidCoordException, BoundsException):
    """Raised if trying to access row.index < 0."""
    ERROR_CODE = "COORD_ROW_INDEX_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coord.row < 0. This outside the dimension of the board."


class RowAboveBoundsException(InvalidCoordException, BoundsException):
    """Raised if trying to access row above array dimension."""
    ERROR_CODE = "COORD_ROW_INDEX_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coord.row > (ROW_SIZE-1). This outside the dimension of the board."


#====================== COORD_COLUMN BOUNDS EXCEPTIONS #======================#
class ColumnBelowBoundsException(InvalidCoordException, BoundsException):
    """Raised if trying to access column.index < 0."""
    ERROR_CODE = "COORD_COLUMN_INDEX_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coordinate.column < 0. This outside the dimension of the board."


class ColumnAboveBoundsException(InvalidCoordException, BoundsException):
    """Raised if trying to access column above array dimension."""
    ERROR_CODE = "COLUMN_ABOVE_INDEX_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coord.column > (COLUMN_SIZE-1). This outside the dimension of the board."