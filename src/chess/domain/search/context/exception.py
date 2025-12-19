# src/chess/domain/searcher/context/collision.py

"""
Module: chess.domain.searcher.context.exception
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""

from chess.system import SearchContextException, NullException, BuildFailedException, ValidationException

__all__ = [
    "ResidentSearchContextException",

    #======= SEARCH_CONTEXT VALIDATION EXCEPTIONS =======#
    "NullResidentSearchContextException",
    "InvalidResidentSearchContextException",
    "NoResidentSearchParamException",
    "ExcessiveResidentSearchParamsException",

    #======= SEARCH_CONTEXT BUILD EXCEPTIONS =======#
    "ResidentSearchContextBuildFailedException",
]


class ResidentSearchContextException(SearchContextException):
    """
    Super class for exceptions raised by ResidentFilter objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging messages.
    """
    ERROR_CODE = "RESIDENT_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "ResidentFilter raised an exception"


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTIONS #======================# 
class NullResidentSearchContextException(ResidentSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team_name residentSearchContext but
    gets validation instead.
    """
    ERROR_CODE = "NULL_SEARCH_RESIDENT_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "ResidentFilter cannot be validation"


class InvalidResidentSearchContextException(ResidentSearchContextException, ValidationException):
    """
    Raised by residentSearchContextBValidator if residentSearchContext fails sanity checks. Exists primarily to
    catch all exceptions raised validating an existing residentSearchContext
    """
    ERROR_CODE = "RESIDENT_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "ResidentFilter validation failed."


class NoResidentSearchParamException(ResidentSearchContextException):
    """
    Raised if all ResidentFilter params are set validation.
    """
    ERROR_CODE = "ZERO_RESIDENT_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "A ResidentFilter cannot have no params selected. Pick one param to run a searcher."
    )

class ExcessiveResidentSearchParamsException(ResidentSearchContextException):
    """
    Raised if more than one ResidentFilter param is set validation.
    """
    ERROR_CODE = "TOO_MANY_RESIDENT_SEARCH_PARAMS_ERROR"
    DEFAULT_MESSAGE = (
        "More than one ResidentFilter param was set. If more than one param is set a searcher cannot be run."
    )


# #======================# RESIDENT_SEARCH_CONTEXT BUILD EXCEPTIONS #======================# 
class ResidentSearchContextBuildFailedException(ResidentSearchContextException, BuildFailedException):
    """"""
    ERROR_CODE = "RESIDENT_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "ResidentFilter build failed."
