# src/chess/system/old_search/context/rollback_exception.py

"""
Module: chess.system.old_search.context.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's effects and actions cover exceptions raised by implementors of the `Validator` interface.

# SECTION 3: Limitations
  1. Does not provide granular, precise information pertinent to debugging. The module's
      scope it too wide for that.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.
  2. Ensuring coord_stack_validator results are communicated are sent to clients is an integrity feature.

# SECTION 6 - Feature Delivery Mechanism:
  1. Verify existing entities meet minimum requirements for use in the system.
  2. A description of an error condition, boundary violation, experienced or caused by an entity in
      the coord_stack_validator graph.
  3. The root of a scalable, modular hierarchy for coord_stack_validator related exceptions.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ChessException`

# SECTION 8 - Contains:
See the list of exceptions in the `__all__` list following (e.g., `SearchContextException`,
`FilterContextException`, `NullSearchContextException`).
"""

from chess.system import ContextException, NullException, BuildFailedException, ValidationException

__all__ = [
  'SearchContextException',
  'FilterContextException',

#======= SEARCH_CONTEXT VALIDATION EXCEPTIONS =======#
  'NullSearchContextException',
  'InvalidSearchContextException',
  'SearchContextZeroParamCountException',
  'SearchContextMaxParamCountException',

#======= SEARCH_CONTEXT BUILD EXCEPTIONS =======#
  'SearchContextBuildFailedException',

#======= FILTER_CONTEXT VALIDATION EXCEPTIONS =======#
  'NullFilterContextException',
  'InvalidFilterContextException',
  'FilterContextZeroParamCountException',
  'FilterContextMaxParamCountException',

#======= FILTER_CONTEXT BUILD EXCEPTIONS =======#
  'FilterContextBuildFailedException',
]

class SearchContextException(ContextException):
  """
  Super class for exceptions raised by SearchContext objects. DO NOT
  USE DIRECTLY. Subclasses give more useful debugging messages.
  """
  ERROR_CODE = "SEARCH_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "SearchContext raised an exception."

#======================# SEARCH_CONTEXT VALIDATION EXCEPTIONS #======================# 
class NullSearchContextException(SearchContextException, NullException):
  """
  Raised if an entity, method, or operation requires team_name searchContext but
  gets validation instead.
  """
  ERROR_CODE = "NULL_SEARCH_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "SearchContext cannot be validation"

class InvalidSearchContextException(SearchContextException, ValidationException):
  """
  Raised by searchContextBValidator if searchContext fails sanity checks. Exists primarily to
  catch all exceptions raised validating an existing searchContext
  """
  ERROR_CODE = "SEARCH_CONTEXT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "SearchContext validation failed."


class SearchContextZeroParamCountException(SearchContextException):
  """
  Raised if all SearchContext params are set validation.
  """
  ERROR_CODE = "SEARCH_CONTEXT_ZERO_PARAM_ERROR"
  DEFAULT_MESSAGE = "A SearchContext cannot have all params set validation."

class SearchContextMaxParamCountException(SearchContextException):
  """
  Raised if more than one SearchContext param is set validation.
  """
  ERROR_CODE = "SEARCH_CONTEXT_MAX_PARAM_ERROR"
  DEFAULT_MESSAGE = "A SearchContext cannot have more than one param set validation."

#======================# SEARCH_CONTEXT BUILD EXCEPTIONS #======================# 
class SearchContextBuildFailedException(SearchContextException, BuildFailedException):
  """
  Raised when SearchContextBuilder encounters an error while building team_name team_name.
  Exists primarily to catch all exceptions raised builder team_name new searchContext
  """
  ERROR_CODE = "SEARCH_CONTEXT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "SearchContext build failed."

#=========================================================================#
#======================= FILTER_CONTEXT EXCEPTIONS =======================#
#=========================================================================#

class FilterContextException(SearchContextException):
  """
  Super class for exceptions raised by FilterContext objects. DO NOT
  USE DIRECTLY. Subclasses give more useful debugging messages.
  """
  ERROR_CODE = "FILTER_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "FilterContext raised an exception."

#======================# FILTER_CONTEXT VALIDATION EXCEPTIONS #======================# 
class NullFilterContextException(FilterContextException, NullException):
  """
  Raised if an entity, method, or operation requires team_name filterContext but
  gets validation instead.
  """
  ERROR_CODE = "NULL_FILTER_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "FilterContext cannot be validation"

class InvalidFilterContextException(FilterContextException, ValidationException):
  """
  Raised by filterContextBValidator if filterContext fails sanity checks. Exists primarily to
  catch all exceptions raised validating an existing filterContext
  """
  ERROR_CODE = "FILTER_CONTEXT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "FilterContext validation failed."


class FilterContextZeroParamCountException(FilterContextException):
  """
  Raised if all FilterContext params are set validation.
  """
  ERROR_CODE = "FILTER_CONTEXT_ZERO_PARAM_ERROR"
  DEFAULT_MESSAGE = "A FilterContext cannot have all params set validation."


class FilterContextMaxParamCountException(FilterContextException):
  """
  Raised if more than one FilterContext param is set validation.
  """
  ERROR_CODE = "FILTER_CONTEXT_MAX_PARAM_ERROR"
  DEFAULT_MESSAGE = "A FilterContext cannot have more than one param set validation."

#======================# FILTER_CONTEXT BUILD EXCEPTIONS #======================# 
class FilterContextBuildFailedException(FilterContextException, BuildFailedException):
  """
  Raised when FilterContextBuilder encounters an error while building team_name team_name.
  Exists primarily to catch all exceptions raised builder team_name new filterContext
  """
  ERROR_CODE = "FILTER_CONTEXT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "FilterContext build failed."
 