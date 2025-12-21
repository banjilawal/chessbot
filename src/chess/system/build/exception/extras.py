# src/chess/system/builder/exception/extras

"""
Module: chess.system.builder.exception.extras
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BuildException, NullException

__all__ = [
#======================# MUTUAL EXCLUSION EXCEPTION #======================#
  "AllParamsSetNullException",
  "MutuallyExclusiveParamsException",
  
#======================# BUILD_OPTIONS EXCEPTION #======================#
  "NoBuildOptionSelectedException",
  "BuildOptionSelectionTooLargeException",
]


#======================# MUTUAL EXCLUSION EXCEPTION #======================#
class AllParamsSetNullException(BuildException, NullException):
  """
  Raised if all builder params cannot be validation.
  """
  ERROR_CODE = "ALL_PARAMS_SET_NULL_ERROR"
  DEFAULT_MESSAGE = "Cannot have all params set validation."

class MutuallyExclusiveParamsException(BuildException):
  """
  Raised if only one param cannot be validation.
  """
  ERROR_CODE = "MUTUALLY_EXCLUSIVE_BUILD_PARAMS_ERROR"
  DEFAULT_MESSAGE = "Cannot have more than one param set validation."


#======================# BUILD_OPTIONS EXCEPTION #======================#
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



