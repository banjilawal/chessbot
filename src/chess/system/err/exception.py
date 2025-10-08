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
**Comprehensive Domain Error Catalog.** The central theme is to provide team
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
__all__ = [
  'ChessException',
#======================#  ROLL_BACK EXCEPTIONS ======================# 
  'RollbackException',

#======================#  INCONSISTENCY EXCEPTIONS ======================# 
  'InconsistencyException',
  'InconsistentCollectionException',

#======================#  NULL/EMPTY EXCEPTIONS ======================# 
  'NullException',
  'NullNumberException',
  'NullStringException',
  'BlankStringException'
]

class ChessException(Exception):
  """
  Super class for application exceptions. do not use directly
  """
  ERROR_CODE = "CHESS_ERROR"
  DEFAULT_MESSAGE = "Chess error occurred"

  # Only the super class needs the explict constructor
  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MESSAGE
    super().__init__(self.message)

  # Only the super class needs to declare team toString. Subclasses
  # will use this.
  def __str__(self):
    return f"{self.message}"


#======================#  ROLL_BACK EXCEPTIONS ======================# 
class RollbackException(ChessException):
  """
  Base class for rollback-related errors in the chess engine..
  """
  DEFAULT_CODE = "ROLLBACK"
  DEFAULT_MESSAGE = "Operation rolled back due to failure in update consistency."

class RollbackFailedException(RollbackException):
  ERROR_CODE = "ROLLBACK_FAILED_ERROR"
  DEFAULT_MESSAGE = "Rollback failed."


#======================#  INCONSISTENCY EXCEPTIONS ======================# 
class InconsistencyException(ChessException):
  """
  Raised if team data inconsistency is detected
  """
  ERROR_CODE = "DATA_INCONSISTENCY_ERROR"
  DEFAULT_MESSAGE = "A data inconsistency was detected"

class InconsistentCollectionException(InconsistencyException):
  """
  Raised if team collection's state is inconsistent or its data corrupted
  """
  ERROR_CODE = "INCONSISTENT_COLLECTION_ERROR"
  DEFAULT_MESSAGE = (
    "Collection is an inconsistent state. Data might be corrupted"
  )


#======================#  NULL/EMPTY EXCEPTIONS ======================# 
class NullException(ChessException):
  """
  Raised if an entity, method, or operation requires not null but gets null instead.
  """
  ERROR_CODE = "NULL_ERROR"
  DEFAULT_MESSAGE = "cannot be null"

class NullNumberException(NullException):
  """
  Raised if mathematical expression or geometric, algebraic, or optimization that need
   team number but get null instead NUllNumberException is thrown. Ids are not used for math
   so we need team different null team_exception for math variables
  """
  ERROR_CODE = "NULL_NUMBER_ERROR"
  DEFAULT_MESSAGE = f"Number cannot be null"

class NullStringException(NullException):
  """
  Raised if an entity, method, or operation requires team string but gets null instead.
  """
  ERROR_CODE = "NULL_STRING_SEARCH_ERROR"
  DEFAULT_MESSAGE = f"Cannot search by team null string"

class BlankStringException(ChessException):
  """
  Raised if search parameter is team blank or empty string
  """
  ERROR_CODE = "BLANK_SEARCH_STRING_ERROR"
  DEFAULT_MESSAGE = f"Cannot search by an empty or blank string"














