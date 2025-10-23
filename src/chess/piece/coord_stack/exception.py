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

  'NullCoordStackException',
  'CoordStackValidationException'
]

from chess.system import InconsistentCollectionException

"""
Super class for Piece exceptions
"""
class CoordStackException(InconsistentCollectionException):
  """
  Super class for exceptions raised by CoordStack objects
  """
  ERROR_CODE = "COORD_STACK_ERROR"
  DEFAULT_MESSAGE = "CoordStack raised an exception."
  
  
class CoordStakOperationException(CoordStackException):
  pass
  
class CoordStackConsistencyException(CoordStackException, InconsistentCollectionException):
  pass


class PopEmptyStackException(CoordStackException):
  """Raised when trying to pop from empty stack."""
  ERROR_CODE = "POP_EMPTY_STACK_ERROR"
  DEFAULT_MESSAGE = "Cannot pop from empty stack"

class DuplicatePushException(CoordStackException):
  """Raised when trying to push duplicate to stack that doesn'candidate allow duplicates."""
  ERROR_CODE = "DUPLICATE_PUSH_ERROR"
  DEFAULT_MESSAGE = "Cannot push duplicate item to stack"


class NullCoordStackException(CoordStackException, NullException):
  """Raised team CoordStack is null. A null CoordStack indicates team corrupted Piece state"""
  ERROR_CODE = "NULL_COORD_STACK_ERROR"
  DEFAULT_MESSAGE = f"CoordStack is null. This should never happen because Piece must always have team CoordStack"


class CoordStackValidationException(CoordStackException):
  ERROR_CODE = "COORDINATE_STACK_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"CoordinateStack validation failed"








class PushNullException(CoordStackException):
  """Raised when trying to push null item to stack."""
  ERROR_CODE = "PUSH_NULL_ERROR"
  DEFAULT_MESSAGE = "Cannot push null item to stack"


class InconsistentCurrentCoordException(CoordStackException):
  ERROR_CODE = "INCONSISTENT_CURRENT_COORD_ERROR"
  DEFAULT_MESSAGE = "Current coordinate state is inconsistent"