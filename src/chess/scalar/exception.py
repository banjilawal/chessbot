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

from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
  'ScalarException',
  
#======================# SCALAR VALIDATION EXCEPTIONS #======================#  
  'NullScalarException',
  'InvalidScalarException',
  
#======================# SCALAR BUILD EXCEPTIONS #======================#  
  'ScalarBuildFailed',

#======================# SCALAR BOUNDS EXCEPTIONS #======================#  
  'ScalarBelowBoundsException',
  'ScalarAboveBoundsException'
]

class ScalarException(ChessException):
  """
  Super class of all exceptions team Scalar object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching all 
  Scalar exceptions.
  """
  ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
  DEFAULT_MESSAGE = "Scalar is below lower bound"
  

#======================# SCALAR VALIDATION EXCEPTIONS #======================#  
class NullScalarException(ScalarException, NullException):
  """Raised if an entity, method, or operation requires team scalar but gets null instead."""
  ERROR_CODE = "NULL_SCALAR_ERROR"
  DEFAULT_MESSAGE = "Scalar cannot be null."

class InvalidScalarException(ScalarException, ValidationException):
  """Raised by ScalaValidators if client fails validation."""
  ERROR_CODE = "SCALAR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Scalar validation failed."


#======================# SCALAR BUILD EXCEPTIONS #======================#  
class ScalarBuildFailed(ScalarException, BuilderException):
  """
  Indicates Scalar could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "SCALAR_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Scalar build failed."


#======================# SCALAR BOUNDS EXCEPTIONS #======================#  
class ScalarBelowBoundsException(ScalarException):
  """Raised if team scalar is below its < -KNIGHT_STEP_SIZE"""
  ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
  DEFAULT_MESSAGE = "Scalar cannot be less than -KNIGHT_STEP_SIZE."

class ScalarAboveBoundsException(ScalarException):
  """Raised if team scalar is above its > KNIGHT_STEP_SIZE"""
  ERROR_CODE = "SCALAR_UPPER_BOUND_ERROR"
  DEFAULT_MESSAGE = "Scalar cannot be greater than KNIGHT_STEP_SIZE."
