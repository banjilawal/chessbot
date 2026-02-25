# src/chess/points/searcher/collision.py

"""
Module: chess.points.searcher.exception
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""

from chess.system import SearchContextException, NullException, BuildException, ValidationException

__all__ = [
    "ResidentSearchContextException",

    #======= SEARCH_CONTEXT VALIDATION EXCEPTION =======#
    "NullResidentSearchContextException",
    "InvalidResidentSearchContextException",
    "NoResidentSearchParamException",
    "ExcessiveResidentSearchParamsException",

    #======= SEARCH_CONTEXT BUILD EXCEPTION =======#
    "ResidentSearchContextBuildException",
]


class ResidentSearchContextException(SearchContextException):
    """
    Super class for exception raised by ResidentFilter objects. DO NOT
    USE DIRECTLY. Subclasses give more useful debugging msgs.
    """
    ERR_CODE = "RESIDENT_SEARCH_CONTEXT_ERROR"
    MSG = "ResidentFilter raised an exception"


# #======================#   SEARCH_CONTEXT VALIDATION EXCEPTION #======================#
class NullResidentSearchContextException(ResidentSearchContextException, NullException):
    """
    Raised if an entity, method, or operation requires team_name residentSearchContext but
    gets validation instead.
    """
    ERR_CODE = "NULL_SEARCH_RESIDENT_CONTEXT_ERROR"
    MSG = "ResidentFilter cannot be validation"


class InvalidResidentSearchContextException(ResidentSearchContextException, ValidationException):
    """
    Raised by residentSearchContextBValidator if residentSearchContext fails sanity checks. Exists primarily to
    catch all exception raised validating an existing residentSearchContext
    """
    ERR_CODE = "RESIDENT_SEARCH_CONTEXT_VALIDATION_ERROR"
    MSG = "ResidentFilter validation failed."


class NoResidentSearchParamException(ResidentSearchContextException):
    """
    Raised if all ResidentFilter params are set validation.
    """
    ERR_CODE = "ZERO_RESIDENT_SEARCH_PARAMS_ERROR"
    MSG = (
        "A ResidentFilter cannot have no params selected. Pick one param to run a searcher."
    )

class ExcessiveResidentSearchParamsException(ResidentSearchContextException):
    """
    Raised if more than one ResidentFilter param is set validation.
    """
    ERR_CODE = "TOO_MANY_RESIDENT_SEARCH_PARAMS_ERROR"
    MSG = (
        "More than one ResidentFilter param was set. If more than one param is set a searcher cannot be run."
    )


# #======================# RESIDENT_SEARCH_CONTEXT BUILD EXCEPTION #======================#
class ResidentSearchContextBuildException(ResidentSearchContextException, BuildException):
    """"""
    ERR_CODE = "RESIDENT_SEARCH_CONTEXT_BUILD_FAILED"
    MSG = "ResidentFilter build failed."
