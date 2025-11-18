# src/chess/system/build/exception.py

"""
Module: chess.system.build.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException, NullException

__all__ = [
  'BuilderException',
  'NullBuilderException',
  'BuildFailedException',
  'AllParamsSetNullException',
  'MutuallyExclusiveParamsException'
]


class BuilderException(ChessException):
  """
  Super class of exceptions organic to `Builder` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `BuilderException` exists primarily to allow catching all `Builder`
  exceptions.
  """
  ERROR_CODE = "BUILDER_ERROR"
  DEFAULT_MESSAGE = "Builder raised an rollback_exception."

class NullBuilderException(BuilderException, NullException):
  """Raised if an entity, method, or operation requires team_name Engine but gets null instead."""
  ERROR_CODE = "NULL_ERROR"
  DEFAULT_MESSAGE = "Builder cannot be null"

class BuildFailedException(BuilderException):
  """
  Raised when team_name Builder encounters an error while building an object. Exists primarily to
  catch all exceptions raised building team_name new objects.
  """
  ERROR_CODE = "BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "build failed."

class AllParamsSetNullException(BuilderException):
  """
  Raised if all build params cannot be null.
  """
  ERROR_CODE = "ALL_PARAMS_SET_NULL_ERROR"
  DEFAULT_MESSAGE = "Cannot have all params set null."

class MutuallyExclusiveParamsException(BuilderException):
  """
  Raised if only one param cannot be null.
  """
  ERROR_CODE = "MUTUALLY_EXCLUSIVE_BUILD_PARAMS_ERROR"
  DEFAULT_MESSAGE = "Cannot have more than one param set null."



