# src/chess.searchContext.exception.py

"""
Module: chess.searchContext.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **SearchContext objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `SearchContextValidator` and `SearchContextBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `SearchContextException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `SearchContext` domain.
It abstracts underlying Python exceptions into domain-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `SearchContextException`,
`NullSearchContextException`, `RowAboveBoundsException`).
"""

from chess.system import ChessException, NullException, BuildFailedException, ValidationException

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
  DEFAULT_MESSAGE = "SearchContext raised an exception"

#======================#  SEARCH_CONTEXT VALIDATION EXCEPTIONS ======================#
class NullSearchContextException(SearchContextException, NullException):
  """
  Raised if an entity, method, or operation requires team searchContext but
  gets null instead.
  """
  ERROR_CODE = "NULL_SEARCH_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "SearchContext cannot be null"

class InvalidSearchContextException(SearchContextException, ValidationException):
  """
  Raised by searchContextBValidator if searchContext fails sanity checks. Exists primarily to
  catch all exceptions raised validating an existing searchContext
  """
  ERROR_CODE = "SEARCH_CONTEXT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "SearchContext validation failed."


class SearchContextZeroParamCountException(SearchContextException):
  """
  Raised if all SearchContext params are set null.
  """
  ERROR_CODE = "SEARCH_CONTEXT_ZERO_PARAM_ERROR"
  DEFAULT_MESSAGE = "A SearchContext cannot have all params set null."

class SearchContextMaxParamCountException(SearchContextException):
  """
  Raised if more than one SearchContext param is set null.
  """
  ERROR_CODE = "SEARCH_CONTEXT_MAX_PARAM_ERROR"
  DEFAULT_MESSAGE = "A SearchContext cannot have more than one param set null."

#======================#  SEARCH_CONTEXT BUILD EXCEPTIONS ======================#
class SearchContextBuildFailedException(SearchContextException, BuildFailedException):
  """
  Raised when SearchContextBuilder encounters an error while building team team.
  Exists primarily to catch all exceptions raised build team new searchContext
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
  DEFAULT_MESSAGE = "FilterContext raised an exception"

#======================#  FILTER_CONTEXT VALIDATION EXCEPTIONS ======================#
class NullFilterContextException(FilterContextException, NullException):
  """
  Raised if an entity, method, or operation requires team filterContext but
  gets null instead.
  """
  ERROR_CODE = "NULL_FILTER_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "FilterContext cannot be null"

class InvalidFilterContextException(FilterContextException, ValidationException):
  """
  Raised by filterContextBValidator if filterContext fails sanity checks. Exists primarily to
  catch all exceptions raised validating an existing filterContext
  """
  ERROR_CODE = "FILTER_CONTEXT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "FilterContext validation failed."


class FilterContextZeroParamCountException(FilterContextException):
  """
  Raised if all FilterContext params are set null.
  """
  ERROR_CODE = "FILTER_CONTEXT_ZERO_PARAM_ERROR"
  DEFAULT_MESSAGE = "A FilterContext cannot have all params set null."


class FilterContextMaxParamCountException(FilterContextException):
  """
  Raised if more than one FilterContext param is set null.
  """
  ERROR_CODE = "FILTER_CONTEXT_MAX_PARAM_ERROR"
  DEFAULT_MESSAGE = "A FilterContext cannot have more than one param set null."

#======================#  FILTER_CONTEXT BUILD EXCEPTIONS ======================#
class FilterContextBuildFailedException(FilterContextException, BuildFailedException):
  """
  Raised when FilterContextBuilder encounters an error while building team team.
  Exists primarily to catch all exceptions raised build team new filterContext
  """
  ERROR_CODE = "FILTER_CONTEXT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "FilterContext build failed."
 