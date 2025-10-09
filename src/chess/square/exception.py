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

from chess.exception import ChessException, BuilderException, NullException, ValidationException

__all__ = [
  'SquareException',

#======================# SQUARE VALIDATION EXCEPTIONS #======================#  
  'NullSquareException',
  'InvalidSquareException',

#======================# SQUARE BUILD EXCEPTIONS #======================#  
  'SquareBuildFailedException'
]

class SquareException(ChessException):
  """
  Super class of all exceptions Square object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching all
  square exceptions.
  """
  ERROR_CODE = "SQUARE_ERROR"
  DEFAULT_MESSAGE = "Square raised an exception."


#======================# SQUARE VALIDATION EXCEPTIONS #======================#  
class NullSquareException(SquareException, NullException):
  """Raised if an entity, method, or operation requires Square but gets null instead."""
  ERROR_CODE = "NULL_SQUARE_ERROR"
  DEFAULT_MESSAGE = "Square cannot be null."

class InvalidSquareException(SquareException, ValidationException):
  """
  Raised by `SquareValidator` if a candidate fails sanity checks. Exists primarily to catch
  all exceptions raised validating an existing `Square` object.
  """
  ERROR_CODE = "SQUARE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Square validation failed."


#======================# SQUARE BUILD EXCEPTIONS #======================# 
class SquareBuildFailedException(SquareException, BuilderException):
  """
  Raised when SquareBuilder encounters an error building a `Square`. Exists primarily
  to catch all exceptions raised creating new `Square`.
  """
  ERROR_CODE = "SQUARE_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Square build failed."
