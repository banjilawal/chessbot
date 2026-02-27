# src/chess/neighbor/searcher/collision.py

"""
Module: chess.neighbor.searcher.exception
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""

from chess.system import SearchContextException, NullException, BuildException, ValidationException

__all__ = [
    "VisitorSearchContextException",

    #======= SEARCH_CONTEXT VALIDATION EXCEPTION =======#
    "NullVisitorSearchContextException",
    "InvalidVisitorSearchContextException",
    "NoVisitorSearchParamException",
    "ArenaVisitorSearchParamsException",

    #======= SEARCH_CONTEXT BUILD EXCEPTION =======#
    "VisitorSearchContextBuildException",
]


class VisitorSearchContextException(SearchContextException):
    """
    Super class for exception raised by VisitorSearchContext objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging msgs.
    """
    ERR_CODE = "VISITOR_SEARCH_CONTEXT_EXCEPTION"
    MSG = "VisitorSearchContext raised an exception"


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTION #======================# 
class NullVisitorSearchContextException(VisitorSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team_name visitorSearchContext but
    gets validation instead.
    """
    ERR_CODE = "NULL_SEARCH_VISITOR_CONTEXT_EXCEPTION"
    MSG = "VisitorSearchContext cannot be validation"


class InvalidVisitorSearchContextException(VisitorSearchContextException, ValidationException):
    """
    Raised by visitorSearchContextBValidator if visitorSearchContext fails sanity checks. Exists primarily to
    catch all exception raised validating an existing visitorSearchContext
    """
    ERR_CODE = "VISITOR_SEARCH_CONTEXT_VALIDATION_EXCEPTION"
    MSG = "VisitorSearchContext validation failed."


class NoVisitorSearchParamException(VisitorSearchContextException):
    """
    Raised if all VisitorSearchContext params are set validation.
    """
    ERR_CODE = "ZERO_VISITOR_SEARCH_PARAMS_EXCEPTION"
    MSG = (
        "A VisitorSearchContext cannot have no params selected. Pick one param to run a searcher."
    )

class ArenaVisitorSearchParamsException(VisitorSearchContextException):
    """
    Raised if more than one VisitorSearchContext param is set validation.
    """
    ERR_CODE = "TOO_MANY_VISITOR_SEARCH_PARAMS_EXCEPTION"
    MSG = (
        "More than one VisitorSearchContext param was set. If more than one param is set a searcher cannot be run."
    )


# #======================# VISITOR_SEARCH_CONTEXT BUILD EXCEPTION #======================# 
class VisitorSearchContextBuildException(VisitorSearchContextException, BuildException):
    """
    Raised when VisitorSearchContextBuilder encounters an error while building team_name team_name.
    Exists primarily to catch all exception raised builder team_name new visitorSearchContext
    """
    ERR_CODE = "VISITOR_SEARCH_CONTEXT_BUILD_FAILED"
    MSG = "VisitorSearchContext build failed."
