# src/chess/vector/collision.py

"""
Module: chess.vector.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException, NullException, ValidationException, BuildFailedException


__all__ = [
  "VectorException",

#====================== NULL VECTOR EXCEPTIONS #======================#
  "NullVectorException",
  
# ====================== VECTOR VALIDATION EXCEPTIONS #======================#
  "InvalidVectorException",

#====================== VECTOR BUILD EXCEPTIONS #======================#  
  "VectorBuildFailedException",

#====================== NULL COMPONENT EXCEPTIONS #======================#  
  "VectorAboveBoundsException",
  "VectorBelowBoundsException",

#====================== VECTOR BOUNDS EXCEPTIONS #======================#  
  "NullXComponentException",
  "NullYComponentException",
]

class VectorException(ChessException):
  """
  Super class of exceptions raised by Scalar objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "VECTOR_ERROR"
  DEFAULT_MESSAGE = "Vector raised an exception."



# ====================== NULL VECTOR EXCEPTIONS #======================#
class NullVectorException(VectorException, NullException):
  """Raised if an entity, method, or operation requires Vector but gets null instead."""
  ERROR_CODE = "NULL_VECTOR_ERROR"
  DEFAULT_MESSAGE = "Vector cannot be null."


# ======================# VECTOR VALIDATION EXCEPTIONS #======================#
class InvalidVectorException(VectorException, ValidationException):
  """Catchall Exception for VectorValidator when a validation candidate fails a sanity check."""
  ERROR_CODE = "VECTOR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Vector validation failed."


#======================# VECTOR BUILD EXCEPTIONS #======================#  
class VectorBuildFailedException(VectorException, BuildFailedException):
  """Catchall Exception for VectorBuilder when it encounters an error building a Vector."""
  ERROR_CODE = "VECTOR_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Vector build failed."


#======================# NULL COMPONENT EXCEPTIONS #======================#  
class NullXComponentException(VectorException, NullException):
  """Raised if Vector's x dimension is null."""
  ERROR_CODE = "VECTOR_NULL_X_DIMENSION_ERROR"
  DEFAULT_MESSAGE = "Vector's X-dimension cannot be null."


class NullYComponentException(VectorException, NullException):
  """Raised if a Vector's y dimension is null."""
  ERROR_CODE = "VECTOR_NULL_Y_DIMENSION_ERROR"
  DEFAULT_MESSAGE = "Vector's Y-dimension cannot be null."


#======================# VECTOR BOUNDS EXCEPTIONS #======================#  
class VectorAboveBoundsException(VectorException):
  """
  A Vector with a component whose magnitude > 7 will cause an ArrayIndexOutOfBounds error when the Vector is
  added or subtracted from a Coord.
  """
  ERROR_CODE = "VECTOR_ABOVE_BOUNDS"
  DEFAULT_MESSAGE = (
    "Vector is above bounds. Arithmetic operations with a Coord will produce a "
    "Coord whose row or column value is outside the Board's range."
  )


class VectorBelowBoundsException(VectorException):
  """
  A Vector with a component whose magnitude < -7 will cause an ArrayIndexOutOfBounds error when the Vector is
  added or subtracted from a Coord.
  """
  ERROR_CODE = "VECTOR_BELOW_BOUNDS_EXCEPTION"
  DEFAULT_MESSAGE = (
    "Vector is below bounds. Arithmetic operations with a Coord will produce a "
    "Coord whose row or column value is outside the Board's range."
  )






