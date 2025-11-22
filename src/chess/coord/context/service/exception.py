# src/chess/coord/context/service/exception.py

"""
Module: chess.coord.context.service.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

__all__ = [
    'SearchContextException',
    'FilterContextException',
    
    # ======= SEARCH_CONTEXT VALIDATION EXCEPTIONS =======#
    'NullSearchContextException',
    'InvalidSearchContextException',
    'SearchContextZeroParamCountException',
    'SearchContextMaxParamCountException',
    
    # ======= SEARCH_CONTEXT BUILD EXCEPTIONS =======#
    'SearchContextBuildFailedException',
    
    # ======= FILTER_CONTEXT VALIDATION EXCEPTIONS =======#
    'NullFilterContextException',
    'InvalidFilterContextException',
    'FilterContextZeroParamCountException',
    'FilterContextMaxParamCountException',
    
    # ======= FILTER_CONTEXT BUILD EXCEPTIONS =======#
    'FilterContextBuildFailedException',
]


# ======================# SEARCH_CONTEXT VALIDATION EXCEPTIONS #======================#
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





# =========================================================================#
# ======================= FILTER_CONTEXT EXCEPTIONS =======================#
# =========================================================================#

class FilterContextException(SearchContextException):
    """
    Super class for exceptions raised by FilterContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "FILTER_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "FilterContext raised an exception."


# ======================# FILTER_CONTEXT VALIDATION EXCEPTIONS #======================#
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


# ======================# FILTER_CONTEXT BUILD EXCEPTIONS #======================#
class FilterContextBuildFailedException(FilterContextException, BuildFailedException):
    """
    Raised when FilterContextBuilder encounters an error while building team_name team_name.
    Exists primarily to catch all exceptions raised builder team_name new filterContext
    """
    ERROR_CODE = "FILTER_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "FilterContext build failed."