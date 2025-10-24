# src/chess/vector/rollback_exception.py

"""
Module: chess.vector.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validation, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each field and behavior in the `Vector` class has an rollback_exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` domain.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` domain.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""

from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'ArenaException',

#====================== ARENA VALIDATION EXCEPTIONS #======================#  
  'NullArenaException',
  'InvalidArenaException',

#====================== ARENA BUILD EXCEPTIONS #======================#  
  'ArenaBuildFailedException',

#====================== COLLECTION_ARENA EXCEPTIONS #======================#  
]

class ArenaException(ChessException):
  """
  Super class exceptions Class object raises organically. Do not use directly. Subclasses give
  details useful for debugging. ClassException exists primarily to allow catching all class
  exceptions.
  """
  ERROR_CODE = "ARENA_ERROR"
  DEFAULT_MESSAGE = "Arena raised an rollback_exception."


#======================# ARENA VALIDATION EXCEPTIONS #======================#  
class NullArenaException(ArenaException, NullException):
  """Raised if an entity, method, or operation requires an arena but gets null instead."""
  ERROR_CODE = "NULL_ARENA_ERROR"
  DEFAULT_MESSAGE = "Arena cannot be null"


class InvalidArenaException(ArenaException, ValidationException):
  """
  Raised by ArenaValidator if arena fails sanity checks. Exists primarily to
  catch all exceptions raised validating an existing arena
  """
  ERROR_CODE = "ARENA_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Arena validation failed"


#======================# ARENA BUILD EXCEPTIONS #======================#  
class ArenaBuildFailedException(ArenaException, BuildFailedException):
  """
  Raised when ArenaBuilder crashed while building team new arena. Exists
  primarily to catch all exceptions raised creating arenas.
  """
  ERROR_CODE = "ARENA_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Arena build failed."