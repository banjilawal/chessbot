# src/chess/coord/exception.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-09-27
version: 1.0.0
"""

from chess.system import BuildFailedException, NullException, ChessException, ValidationException

__all__ = [
    "CoordException",
    
    # ====================== NULL COORD EXCEPTIONS #======================#
    "NullCoordException",
    
    # ====================== COORD VALIDATION EXCEPTIONS #======================#
    "InvalidCoordException",
    
    # ====================== COORD_ROW VALIDATION EXCEPTIONS #======================#
    "NullRowException",
    "RowBelowBoundsException",
    "RowAboveBoundsException",
    
    # ====================== COORD_COLUMN VALIDATION EXCEPTIONS #======================#
    "NullColumnException",
    "ColumnAboveBoundsException",
    "ColumnBelowBoundsException",
    
    # ====================== COORD BUILD EXCEPTIONS #======================#
    "CoordBuildFailedException"
]


class CoordException(ChessException):
    """
    Super class of exceptions raised by Scalar objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "COORD_ERROR"
    DEFAULT_MESSAGE = f"Invalid Coord state threw an err"


# ====================== NULL COORD EXCEPTIONS #======================#
class NullCoordException(CoordException, NullException):
    """Raised if an entity, method, or operation requires Coord but gets null instead."""
    ERROR_CODE = "NULL_COORD_ERROR"
    DEFAULT_MESSAGE = "Coord cannot be null"


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


class RowBelowBoundsException(CoordException):
    """Raised if trying to access row.index < 0."""
    ERROR_CODE = "COORD_ROW_INDEX_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coord.row < 0. This outside the dimension of the board."


class RowAboveBoundsException(CoordException):
    """Raised if trying to access row above array dimension."""
    ERROR_CODE = "COORD_ROW_INDEX_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coord.row > (ROW_SIZE-1). This outside the dimension of the board."


# ====================== COORD_COLUMN VALIDATION EXCEPTIONS #======================#
class NullColumnException(NullException):
    """Raised if Coord.row is null."""
    ERROR_CODE = "NULL_COORD_COLUMN_INDEX_ERROR"
    DEFAULT_MESSAGE = "Coord.column property cannot be null."


class ColumnBelowBoundsException(CoordException):
    """Raised if trying to access column.index < 0."""
    ERROR_CODE = "COORD_COLUMN_INDEX_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coordinate.column < 0. This outside the dimension of the board."


class ColumnAboveBoundsException(CoordException):
    """Raised if trying to access column above array dimension."""
    ERROR_CODE = "COLUMN_ABOVE_INDEX_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Coord.column > (COLUMN_SIZE-1). This outside the dimension of the board."


# ====================== COORD BUILD EXCEPTIONS #======================#
class CoordBuildFailedException(CoordException, BuildFailedException):
    """Catchall Exception for CoordBuilder when it stops because of an error."""
    ERROR_CODE = "COORD_BUILD_FAILED"
    DEFAULT_MESSAGE = "Coord build failed."
