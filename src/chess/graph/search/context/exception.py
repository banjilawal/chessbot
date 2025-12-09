# src/chess/neighbor/searcher/context/collision.py

"""
Module: chess.neighbor.searcher.context.exception
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""

from chess.system import SearchContextException, NullException, BuildFailedException, ValidationException

__all__ = [
    "VisitorSearchContextException",

    #======= SEARCH_CONTEXT VALIDATION EXCEPTIONS =======#
    "NullVisitorSearchContextException",
    "InvalidVisitorSearchContextException",
    "NoVisitorSearchParamException",
    "TooManyVisitorSearchParamsException",

    #======= SEARCH_CONTEXT BUILD EXCEPTIONS =======#
    "VisitorSearchContextBuildFailedException",
]


class VisitorSearchContextException(SearchContextException):
    """
    Super class for exceptions raised by VisitorSearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "VISITOR_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "VisitorSearchContext raised an exception"


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTIONS #======================# 
class NullVisitorSearchContextException(VisitorSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team_name visitorSearchContext but
    gets validation instead.
    """
    ERROR_CODE = "NULL_SEARCH_VISITOR_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "VisitorSearchContext cannot be validation"


class InvalidVisitorSearchContextException(VisitorSearchContextException, ValidationException):
    """
    Raised by visitorSearchContextBValidator if visitorSearchContext fails sanity checks. Exists primarily to
    catch all exceptions raised validating an existing visitorSearchContext
    """
    ERROR_CODE = "VISITOR_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "VisitorSearchContext validation failed."


class NoVisitorSearchParamException(VisitorSearchContextException):
    """
    Raised if all VisitorSearchContext params are set validation.
    """
    ERROR_CODE = "ZERO_VISITOR_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "A VisitorSearchContext cannot have no params selected. Pick one param to run a searcher."
    )

class TooManyVisitorSearchParamsException(VisitorSearchContextException):
    """
    Raised if more than one VisitorSearchContext param is set validation.
    """
    ERROR_CODE = "TOO_MANY_VISITOR_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one VisitorSearchContext param was set. If more than one param is set a searcher cannot be run."
    )


# #======================# VISITOR_SEARCH_CONTEXT BUILD EXCEPTIONS #======================# 
class VisitorSearchContextBuildFailedException(VisitorSearchContextException, BuildFailedException):
    """
    Raised when VisitorSearchContextBuilder encounters an error while building team_name team_name.
    Exists primarily to catch all exceptions raised builder team_name new visitorSearchContext
    """
    ERROR_CODE = "VISITOR_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "VisitorSearchContext build failed."
