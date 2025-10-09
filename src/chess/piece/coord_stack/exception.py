# src/chess/vector/exception.py

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