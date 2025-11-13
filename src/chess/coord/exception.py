# src/chess/coord/exception.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validator, and manipulation of Coord objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
Coord, CoordBuilder, and CoordValidator

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each consistency and behavior in the Coord class has an rollback_exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the Coord graph.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the Coord graph.
4. Providing a clear distinction between errors related to Coord instances and
    errors from Python, the Operating System or elsewhere in the ChessBot application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From chess.system:
  * Exceptions: ChessException, ValidationException, NullException,
        BuildFailedException.

CONTAINS:
--------
See the list of exceptions in the __all__ list following (e.g., CoordException,
NullCoordException, InvalidCoordException, ).
"""


from chess.system import BuildFailedException, NullException, ChessException, ValidationException


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
  Super class of exceptions raised by Coord objects. Do not use directly. Subclasses give 
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "COORD_ERROR"
  DEFAULT_MESSAGE = f"Invalid Coord state threw an err"


# ====================== NULL COORD VALIDATION EXCEPTIONS #======================#
class NullCoordException(CoordException, NullException):
  """Raised if an entity, method, or operation requires Coord but gets null instead."""
  ERROR_CODE = "NULL_COORD_ERROR"
  DEFAULT_MESSAGE = "Coord cannot be null"


# ====================== COORD VALIDATION EXCEPTIONS #======================#
class InvalidCoordException(CoordException, ValidationException):
  """Catchall Exception for CoordValidator when a validation candidate fails a sanity check."""
  ERROR_CODE = "COORD_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Coord validation failed."


#====================== COORD_ROW VALIDATION EXCEPTIONS #======================#  
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


#====================== COORD_COLUMN VALIDATION EXCEPTIONS #======================#  
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


#====================== COORD BUILD EXCEPTIONS #======================#  
class CoordBuildFailedException(CoordException, BuildFailedException):
  """Catchall Exception for CoordBuilder when it stops because of an error."""
  ERROR_CODE = "COORD_BUILD_FAILED"
  DEFAULT_MESSAGE = "Coord build failed."