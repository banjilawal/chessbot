from chess.system import ROW_SIZE, COLUMN_SIZE
from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
  'CoordException',

  'NullCoordException',
  'InvalidCoordException',

  'CoordBuildFailed',

  'NullRowException',
  'RowBelowBoundsException',
  'RowAboveBoundsException',

  'NullColumnException',
  'ColumnAboveBoundsException',
  'ColumnBelowBoundsException',
]

class CoordException(ChessException):
  """
  Super class for Coord related exceptions.
  """
  ERROR_CODE = "COORD_ERROR"
  DEFAULT_MESSAGE = f"Invalid Coord state threw an err"

class NullCoordException(CoordException, NullException):
  """Raised by methods, entities, and models that require a Coord but receive a null."""
  ERROR_CODE = "NULL_COORD_ERROR"
  DEFAULT_MESSAGE = "Coord cannot be null"


class InvalidCoordException(CoordException, ValidationException):
  """Raised by CoordValidator if client fails validation."""
  ERROR_CODE = "COORD_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Coord validation failed"

class CoordBuildFailed(CoordException, BuilderException):
  """
  Indicates Coord could not be built. Wraps and re-raises
  errors that occurred during creation.
  """
  ERROR_CODE = "COORD_BUILD_FAILED"
  DEFAULT_MESSAGE = "Coord build failed."

class NullRowException(NullException):
  """
  Raised if a row is null. A coord cannot be created if the row is null
  """
  ERROR_CODE = "NULL_ROW_ERROR"
  DEFAULT_MESSAGE = "Row cannot be null"


class RowBelowBoundsException(CoordException):
  """
  If row < 0 RowBelowBoundsException is raised. Domain specific alternative
  to ArrayIndexOutOfBoundsException
  """
  ERROR_CODE = "ROW_BELOW_BOUNDS_ERROR"
  DEFAULT_MESSAGE = f"Coord.row < 0. This outside the dimension of the board"


class RowAboveBoundsException(CoordException):
  """
  If a row >= ROW_SIZE RowAboveBoundsException is raised.
  """
  ERROR_CODE = "ROW_ABOVE_BOUNDS_ERROR"
  DEFAULT_MESSAGE = f"Coord.row > {ROW_SIZE - 1}. This outside the dimension of the board"


class NullColumnException(NullException):
  """
  Raised if a column is null. A coord cannot be created if the column is null
  """
  ERROR_CODE = "NULL_COLUMN_ERROR"
  DEFAULT_MESSAGE = "Column cannot be null"


class ColumnBelowBoundsException(CoordException):
  """
  If Coord.column < 0 ColumnBelowBoundsException is raised.
  """
  ERROR_CODE = "COLUMN_BELOW_BOUNDS_ERROR"
  DEFAULT_MESSAGE = f"Coordinate.column < 0. This outside the dimension of the board"


class ColumnAboveBoundsException(CoordException):
  """
  If Coord.column > DIMENSION ColumnAboveBoundsException is raised.
  """
  ERROR_CODE = "COLUMN_ABOVE_BOUNDS_ERROR"
  DEFAULT_MESSAGE = f"Coord.column > {COLUMN_SIZE-1}. This outside the dimension of the board"