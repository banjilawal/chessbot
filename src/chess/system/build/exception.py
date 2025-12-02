# src/chess/system/builder/exception.py

"""
Module: chess.system.builder.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException, NullException, ValidationException

__all__ = [
# ======================# BUILDER EXCEPTION SUPER_CLASS #======================#
  "BuilderException",
  
# ======================# BUILDER VALIDATION EXCEPTIONS #======================#
  "InvalidBuilderException",
  "NullBuilderException",
  
# ======================# FAILED BUILD OPERATION EXCEPTION #======================#
  "BuildFailedException",
  
# ======================# MUTUAL EXCLUSION EXCEPTIONS #======================#
  "AllParamsSetNullException",
  "MutuallyExclusiveParamsException",
  
# ======================# BUILD_OPTIONS EXCEPTIONS #======================#
  "NoBuildOptionSelectedException",
  "BuildOptionSelectionTooLargeException",
]


# ======================# BUILDER EXCEPTION SUPER_CLASS #======================#
class BuilderException(ChessException):
  """
  Super class of exceptions organic to Builder objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `BuilderException` exists primarily to allow catching all `Builder`
  exceptions.
  """
  ERROR_CODE = "BUILDER_ERROR"
  DEFAULT_MESSAGE = "Builder raised an exception."


# ======================# BUILDER VALIDATION EXCEPTIONS #======================#
class InvalidBuilderException(BuilderException, ValidationException):
  """Raised if an entity, method, or operation requires team_name Engine but gets null instead."""
  ERROR_CODE = "NULL_ERROR"
  DEFAULT_MESSAGE = "Builder cannot be validation"

class NullBuilderException(InvalidBuilderException, NullException):
  """Raised if an entity, method, or operation requires team_name Engine but gets null instead."""
  ERROR_CODE = "NULL_ERROR"
  DEFAULT_MESSAGE = "Builder cannot be validation"


# ======================# FAILED BUILD OPERATION EXCEPTION #======================#
class BuildFailedException(BuilderException):
  """Raised when an error halts an object's build process."""
  ERROR_CODE = "BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "build failed."


# ======================# MUTUAL EXCLUSION EXCEPTIONS #======================#
class AllParamsSetNullException(BuilderException, NullException):
  """
  Raised if all builder params cannot be validation.
  """
  ERROR_CODE = "ALL_PARAMS_SET_NULL_ERROR"
  DEFAULT_MESSAGE = "Cannot have all params set validation."

class MutuallyExclusiveParamsException(BuilderException):
  """
  Raised if only one param cannot be validation.
  """
  ERROR_CODE = "MUTUALLY_EXCLUSIVE_BUILD_PARAMS_ERROR"
  DEFAULT_MESSAGE = "Cannot have more than one param set validation."


# ======================# BUILD_OPTIONS EXCEPTIONS #======================#
class NoBuildOptionSelectedException(BuilderException):
  """
  Raised when none of the possible options required to builder an object are selected.
  Mainly used by Context classes
  """
  ERROR_CODE = "NO_BUILD_OPTION_SELECTED_ERROR"
  DEFAULT_MESSAGE = "None of the options required for the builder were."


class BuildOptionSelectionTooLargeException(BuilderException):
  """Raised when too many of the available builder options are selected. Mainly used by Context classes."""
  ERROR_CODE = "TOO_MANY_BUILD_OPTIONS_SELECTED_ERROR"
  DEFAULT_MESSAGE = "Too many builder options were selected."



