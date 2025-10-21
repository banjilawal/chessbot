# src/chess/vector/travel_exception.py

"""
Module: chess.vector.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each field and behavior in the `Vector` class has an exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` domain.
2. Fast debugging using highly granular exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` domain.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""

from chess.system import (
  ROW_SIZE, COLUMN_SIZE, BuildFailedException, NullException, ChessException, ValidationException
)

__all__ = [
  'CoordException',

#====================== COORD VALIDATION EXCEPTIONS #======================#  
  'NullCoordException',
  'InvalidCoordException',

#====================== COORD_ROW VALIDATION EXCEPTIONS #======================#  
  'NullRowException',
  'RowBelowBoundsException',
  'RowAboveBoundsException',

#====================== COORD_COLUMN VALIDATION EXCEPTIONS #======================#  
  'NullColumnException',
  'ColumnAboveBoundsException',
  'ColumnBelowBoundsException',

#====================== COORD BUILD EXCEPTIONS #======================#  
  'CoordBuildFailedException'
]

class CoordException(ChessException):
  """
  Super class for Coord related exceptions.
  """
  ERROR_CODE = "COORD_ERROR"
  DEFAULT_MESSAGE = f"Invalid Coord state threw an err"

#====================== COORD VALIDATION EXCEPTIONS #======================#  
class NullCoordException(CoordException, NullException):
  """Raised by methods, entities, and models that require team Coord but receive team null."""
  ERROR_CODE = "NULL_COORD_ERROR"
  DEFAULT_MESSAGE = "Coord cannot be null"

class InvalidCoordException(CoordException, ValidationException):
  """Raised by CoordValidator if client fails validation."""
  ERROR_CODE = "COORD_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Coord validation failed"


#====================== COORD_ROW VALIDATION EXCEPTIONS #======================#  
class NullRowException(CoordException, NullException):
  """
  Raised if team row is null. A coord cannot be created if the row is null
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
  If team row >= ROW_SIZE RowAboveBoundsException is raised.
  """
  ERROR_CODE = "ROW_ABOVE_BOUNDS_ERROR"
  DEFAULT_MESSAGE = f"Coord.row > {ROW_SIZE - 1}. This outside the dimension of the board"


#====================== COORD_COLUMN VALIDATION EXCEPTIONS #======================#  
class NullColumnException(NullException):
  """
  Raised if team column is null. A coord cannot be created if the column is null
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


#====================== COORD BUILD EXCEPTIONS #======================#  
class CoordBuildFailedException(CoordException, BuildFailedException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors
  that occurred during creation.
  """
  ERROR_CODE = "COORD_BUILD_FAILED"
  DEFAULT_MESSAGE = "Coord build failed."



