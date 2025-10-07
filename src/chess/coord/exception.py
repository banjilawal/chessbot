# src/chess.coord.exception.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide a
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` domain.
It abstracts underlying Python exceptions into domain-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""

from chess.system import (
  ROW_SIZE, COLUMN_SIZE, BuildFailedException, NullException, ChessException, ValidationException
)

__all__ = [
  'CoordException',

#====================== COORD VALIDATION EXCEPTIONS ======================# 
  'NullCoordException',
  'InvalidCoordException',


#====================== COORD_ROW VALIDATION EXCEPTIONS ======================# 
  'NullRowException',
  'RowBelowBoundsException',
  'RowAboveBoundsException',

#====================== COORD_COLUMN VALIDATION EXCEPTIONS ======================# 
  'NullColumnException',
  'ColumnAboveBoundsException',
  'ColumnBelowBoundsException',

#====================== COORD BUILD EXCEPTIONS ======================# 
  'CoordBuildFailedException'
]

class CoordException(ChessException):
  """
  Super class for Coord related exceptions.
  """
  ERROR_CODE = "COORD_ERROR"
  DEFAULT_MESSAGE = f"Invalid Coord state threw an err"

#====================== COORD VALIDATION EXCEPTIONS ======================# 
class NullCoordException(CoordException, NullException):
  """Raised by methods, entities, and models that require a Coord but receive a null."""
  ERROR_CODE = "NULL_COORD_ERROR"
  DEFAULT_MESSAGE = "Coord cannot be null"

class InvalidCoordException(CoordException, ValidationException):
  """Raised by CoordValidator if client fails validation."""
  ERROR_CODE = "COORD_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Coord validation failed"


#====================== COORD_ROW VALIDATION EXCEPTIONS ======================# 
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


#====================== COORD_COLUMN VALIDATION EXCEPTIONS ======================# 
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


#====================== COORD BUILD EXCEPTIONS ======================# 
class CoordBuildFailedException(CoordException, BuildFailedException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors
  that occurred during creation.
  """
  ERROR_CODE = "COORD_BUILD_FAILED"
  DEFAULT_MESSAGE = "Coord build failed."



