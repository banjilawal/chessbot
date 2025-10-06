from chess.system import ROW_SIZE, COLUMN_SIZE, BuildFailedException, NullException, ChessException, ValidationException

__all__ = [
  'CoordException',

  # === COORD VALIDATION EXCEPTIONS ===
  'NullCoordException',
  'InvalidCoordException',


  # === COORD_ROW VALIDATION EXCEPTIONS ===
  'NullRowException',
  'RowBelowBoundsException',
  'RowAboveBoundsException',

  # === COORD_COLUMN VALIDATION EXCEPTIONS ===
  'NullColumnException',
  'ColumnAboveBoundsException',
  'ColumnBelowBoundsException',

  # === COORD BUILD EXCEPTIONS ===
  'CoordBuildFailedException'
]

class CoordException(ChessException):
  """
  Super class for Coord related exceptions.
  """
  ERROR_CODE = "COORD_ERROR"
  DEFAULT_MESSAGE = f"Invalid Coord state threw an err"

  # === COORD VALIDATION EXCEPTIONS ===
class NullCoordException(CoordException, NullException):
  """Raised by methods, entities, and models that require a Coord but receive a null."""
  ERROR_CODE = "NULL_COORD_ERROR"
  DEFAULT_MESSAGE = "Coord cannot be null"

class InvalidCoordException(CoordException, ValidationException):
  """Raised by CoordValidator if client fails validation."""
  ERROR_CODE = "COORD_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Coord validation failed"


  # === COORD_ROW VALIDATION EXCEPTIONS ===
  class NullRowException(CoordException, NullException):
    """
    Raised if a row is null. A coord cannot be created if the row is null
    """
    ERROR_CODE = "NULL_ROW_ERROR"
    DEFAULT_MESSAGE = "Row cannot be null."

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


  # === COORD_COLUMN VALIDATION EXCEPTIONS ===
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
  DEFAULT_MESSAGE = f"Coord.column > {COLUMN_SIZE - 1}. This outside the dimension of the board"


  # === COORD BUILD EXCEPTIONS ===
class CoordBuildFailedException(CoordException, BuildFailedException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors
  that occurred during creation.
  """
  ERROR_CODE = "COORD_BUILD_FAILED"
  DEFAULT_MESSAGE = "Coord build failed."



