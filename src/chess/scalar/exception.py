# chess/scalar/exception.py

"""
Module: chess.scalar.exception
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""

from chess.system import ChessException, NullException, ValidationException, BuildFailedException

__all__ = [
  "ScalarException",
  
#======================# SCALAR VALIDATION EXCEPTIONS #======================#  
  "NullScalarException",
  "InvalidScalarException",
  
#======================# SCALAR BUILD EXCEPTIONS #======================#  
  "ScalarBuildFailedException",

#======================# SCALAR BOUNDS EXCEPTIONS #======================#  
  "ScalarBelowBoundsException",
  "ScalarAboveBoundsException"
]

class ScalarException(ChessException):
  """
  Super class of exceptions raised by Scalar objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
  DEFAULT_MESSAGE = "Scalar is below lower bound"
  

#======================# NULL SCALAR EXCEPTIONS #======================#
class NullScalarException(ScalarException, NullException):
  """Raised if an entity, method, or operation requires Board but gets null instead."""
  ERROR_CODE = "NULL_SCALAR_ERROR"
  DEFAULT_MESSAGE = "Scalar cannot be null."


#======================# SCALAR VALIDATION EXCEPTIONS #======================#
class InvalidScalarException(ScalarException, ValidationException):
  """Catchall Exception for BoardValidator when a validation candidate fails a sanity check."""
  ERROR_CODE = "SCALAR_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Scalar validation failed."


#======================# SCALAR BUILD EXCEPTIONS #======================#
class ScalarBuildFailedException(ScalarException, BuildFailedException):
  """Catchall Exception for BoardBuilder when it encounters an error building a Board."""
  ERROR_CODE = "SCALAR_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Scalar build failed."


#======================# SCALAR BOUNDS EXCEPTIONS #======================#  
class ScalarBelowBoundsException(ScalarException):
  """Raised if team_name scalar is below its < -KNIGHT_STEP_SIZE"""
  ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
  DEFAULT_MESSAGE = "Scalar cannot be less than -KNIGHT_STEP_SIZE."

class ScalarAboveBoundsException(ScalarException):
  """Raised if team_name scalar is above its > KNIGHT_STEP_SIZE"""
  ERROR_CODE = "SCALAR_UPPER_BOUND_ERROR"
  DEFAULT_MESSAGE = "Scalar cannot be greater than KNIGHT_STEP_SIZE."
