# chess/system/context/exception.py

"""
Module: chess.system.context.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException, NullException, BuildFailedException, ValidationException

__all__ = [
  'ContextException',

#======================# CONTEXT VALIDATION EXCEPTIONS #======================#  
  'NullContextException',
  'InvalidContextException',

#======================# CONTEXT BUILD EXCEPTIONS #======================#  
  'ContextBuildFailedException',
]

class ContextException(ChessException):
  """
  Super class for exceptions raised by Context objects. DO NOT
  USE DIRECTLY. Subclasses give more useful debugging messages.
  """
  ERROR_CODE = "CONTEXT_ERROR"
  DEFAULT_MESSAGE = "Context raised an rollback_exception"

#======================# CONTEXT VALIDATION EXCEPTIONS #======================#  
class NullContextException(ContextException, NullException):
  """
  Raised if an entity, method, or operation requires team_name context but
  gets null instead.
  """
  ERROR_CODE = "NULL_CONTEXT_ERROR"
  DEFAULT_MESSAGE = f"Context cannot be null"

class InvalidContextException(ContextException, ValidationException):
  """
  Raised by contextBValidator if context fails sanity checks. Exists primarily to
  catch all exceptions raised validating an existing context
  """
  ERROR_CODE = "CONTEXT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Context validator failed."

#======================# CONTEXT BUILD EXCEPTIONS #======================#  
class ContextBuildFailedException(ContextException, BuildFailedException):
  """
  Raised when ContextBuilder encounters an error while building team_name team_name.
  Exists primarily to catch all exceptions raised build team_name new context
  """
  ERROR_CODE = "CONTEXT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Context build failed."