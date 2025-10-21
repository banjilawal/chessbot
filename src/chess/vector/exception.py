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

from chess.system import ChessException, NullException, ValidationException, BuildFailedException


__all__ = [
  'VectorException',

#====================== VECTOR VALIDATION EXCEPTIONS #======================#  
  'NullVectorException',
  'InvalidVectorException',

#====================== VECTOR BUILD EXCEPTIONS #======================#  
  'VectorBuildFailedException',

#====================== NULL COMPONENT EXCEPTIONS #======================#  
  'VectorAboveBoundsException',
  'VectorBelowBoundsException',

#====================== VECTOR BOUNDS EXCEPTIONS #======================#  
  'NullXComponentException',
  'NullYComponentException',
]

class VectorException(ChessException):
  """
  Super class of exceptions organic to `Vector` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `VectorException` exists primarily to allow catching all `Vector`
  exceptions.
  """
  ERROR_CODE = "VECTOR_ERROR"
  DEFAULT_MESSAGE = "Vector raised an exception."


#======================# VECTOR VALIDATION EXCEPTIONS #======================#  
class NullVectorException(VectorException, NullException):
  """Raised if an entity, method, or operation requires team vector but gets null instead."""
  ERROR_CODE = "NULL_VECTOR_ERROR"
  DEFAULT_MESSAGE = "Vector cannot be null"


class InvalidVectorException(VectorException, ValidationException):
  """
  Raised by VectorValidator if `Vector` fails sanity checks. Exists primarily to catch all
  exceptions raised validating an existing `Vector`
  """
  ERROR_CODE = "VECTOR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Vector validation failed"


#======================# VECTOR BUILD EXCEPTIONS #======================#  
class VectorBuildFailedException(VectorException, BuildFailedException):
  """
  Raised when VectorBuilder crashed while building a new vector. Exists
  primarily to catch all exceptions raised creating vectors.
  """
  ERROR_CODE = "VECTOR_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Vector build failed."


#======================# NULL COMPONENT EXCEPTIONS #======================#  
class NullXComponentException(VectorException, NullException):
  """Raised if team vector's x dimension is null"""
  ERROR_CODE = "VECTOR_NULL_X_DIMENSION_ERROR"
  DEFAULT_MESSAGE = "Vector's X-dimension cannot be null"


class NullYComponentException(VectorException, NullException):
  """Raised if team vector's y dimension is null"""
  ERROR_CODE = "VECTOR_NULL_Y_DIMENSION_ERROR"
  DEFAULT_MESSAGE = "Vector's Y-dimension cannot be null"


#======================# VECTOR BOUNDS EXCEPTIONS #======================#  
class VectorAboveBoundsException(VectorException):
  """
  Iterating across coordinates to examine squares chess pieces can explore their with team step no
  larger than the knight's number of rows o squares covered in team move. If team vector's x value is
  larger than KNIGHT SIZE raise this err
  """
  ERROR_CODE = "VECTOR_ABOVE_BOUNDS"
  DEFAULT_MESSAGE = "Vector above bounds"


class VectorBelowBoundsException(VectorException):
  """
  Iterating across coordinates to examine squares chess pieces can explore their with team step no
  larger than the knight's number of rows o squares covered in team move. If team vector's x value is
  larger than KNIGHT SIZE raise this err
  """
  ERROR_CODE = "VECTOR_BELOW_BOUNDS_EXCEPTION"
  DEFAULT_MESSAGE = "Vector is below bounds"






