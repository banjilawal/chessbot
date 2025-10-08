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

from chess.exception import ChessException, ValidationException, NullException

__all__ = [
  'CoordStackException',
  'DoubleCoordPushException',
  'NullCoordStackException',
  'CoordStackValidationException'
]

"""
Super class for Piece exceptions
"""
class CoordStackException(ChessException):
  """
  Super class for exceptions raised by CoordStack objects
  """
  ERROR_CODE = "COORD_STACK_ERROR"
  DEFAULT_MESSAGE = "CoordStack raised an exception."


class DoubleCoordPushException(CoordStackException):
  """
  Raised when team Coord at the top of the stack is pushed again. This is additional sanity check.
  Piece should catch moving to the same Square before the stack is modified. important in OccupationEvent
  transactions
  """
  ERROR_CODE = "DOUBLE_COORD_PUSH_ERROR"
  DEFAULT_MESSAGE = "Cannot push the same Coord twice. The Coord is already at the top of the stack"


class NullCoordStackException(CoordStackException, NullException):
  """Raised team CoordStack is null. A null CoordStack indicates team corrupted Piece state"""
  ERROR_CODE = "NULL_COORD_STACK_ERROR"
  DEFAULT_MESSAGE = f"CoordStack is null. This should never happen because Piece must always have team CoordStack"


class CoordStackValidationException(CoordStackException, ValidationException):
  ERROR_CODE = "COORDINATE_STACK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"CoordinateStack validation failed"