from chess.common import ROW_SIZE, COLUMN_SIZE
from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
    'CoordException',
    'ColumnAboveBoundsException',
    'ColumnBelowBoundsException',
    'CoordValidationException',
    'CoordBuilderException',
    'NullCoordBuilderException',
    'RowAboveBoundsException',
    'RowBelowBoundsException',
    'NullRowException',
    'NullCoordStackException'
]

"""
Super class for Coord related exceptions
"""
class CoordException(ChessException):
    """
    Super class for Coord related exceptions.

    Subclasses:
        - RowBelowBoundsException
        - RowAboveBoundsException
        - ColumnBelowBoundsException
        - ColumnAboveBoundsException
    """
    ERROR_CODE = "COORD_ERROR"
    DEFAULT_MESSAGE = f"Invalid Coord state threw an exception"


class ColumnAboveBoundsException(CoordException):
    """
    If Coord.column > DIMENSION ColumnAboveBoundsException is raised.
    """
    ERROR_CODE = "COLUMN_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coord.column > {COLUMN_SIZE-1}. This outside the dimension of the board"


class ColumnBelowBoundsException(CoordException):
    """
    If Coord.column < 0 ColumnBelowBoundsException is raised.
    """
    ERROR_CODE = "COLUMN_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coordinate.column < 0. This outside the dimension of the board"


class CoordValidationException(ValidationException):
    ERROR_CODE = "COORDINATE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Coordinate validation failed"


class CoordBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when CoordBuilder runs.
    """
    ERROR_CODE = "COORD_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CoordBuilder raised an exception"


class NullCoordBuilderException(NullException):
    """
    Raised if a CoordBuilder is null.
    """
    ERROR_CODE = "NULL_COORD_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CoordBuilder cannot be null"


class RowAboveBoundsException(CoordException):
    """
    If a row >= ROW_SIZE RowAboveBoundsException is raised.
    """
    ERROR_CODE = "ROW_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coord.row > {ROW_SIZE - 1}. This outside the dimension of the board"


class RowBelowBoundsException(CoordException):
    """
    If row < 0 RowBelowBoundsException is raised. Domain specific alternative
    to ArrayIndexOutOfBoundsException
    """
    ERROR_CODE = "ROW_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coord.row < 0. This outside the dimension of the board"


class NullRowException(NullException):
    """
    Raised if a row is null. A coord cannot be created if the row is null
    """
    ERROR_CODE = "NULL_ROW_ERROR"
    DEFAULT_MESSAGE = f"Row cannot be null"


class NullCoordStackException(NullException):
    """
    Raised if a discovery's CoordStack (Piece.positions) is null.
    """
    ERROR_CODE = "NULL_COORD_STACK_ERROR"
    DEFAULT_MESSAGE = f"CoordStack cannot be null"



class NullCoordException(NullException):
    """
    Raised if a coord is null
    """
    ERROR_CODE = "NULL_COORDINATE_ERROR"
    DEFAULT_MESSAGE = f"Coordinate cannot be null"


class NullColumnException(NullException):
    """
    Raised if a column is null. A coord cannot be created if the column is null
    """
    ERROR_CODE = "NULL_COLUMN_ERROR"
    DEFAULT_MESSAGE = f"Column cannot be null"