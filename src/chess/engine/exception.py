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

__all__ = [
  'EngineException',
#======================# ENGINE VALIDATION EXCEPTIONS #======================#  
  'NullEngineException',
#======================# ENGINE BUILD EXCEPTIONS #======================#  
  'BuildFailedException'
]

from chess.system import ChessException, NullException, BuildFailedException

class EngineException(ChessException):
  """
  Super class of exceptions organic to `Engine` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `EngineException` exists primarily to allow catching all `Engine`
  exceptions.
  """
  ERROR_CODE = "ENGINE_ERROR"
  DEFAULT_MESSAGE = "Engine raised an exception."

class NullEngineException(EngineException, NullException):
  """Raised if an entity, method, or operation requires an `Engine` but gets null instead."""
  ERROR_CODE = "NULL_ENGINE_ERROR"
  DEFAULT_MESSAGE = "Engine cannot be null"

class EngineBuildFailed(EngineException, BuildFailedException):
  """
  Raised when `EngineBuilder` crashed while building team new object. Exists
  primarily to catch all exceptions raised creating engines.
  """
  ERROR_CODE = "ENGINE_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Engine build failed."