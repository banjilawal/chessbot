# src/square/search/context/collision.py

"""
Module: chess.square.search.context.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


from chess.system import (
    BuildOptionSelectionTooLargeException, ContextException, NoBuildOptionSelectedException, NullException,
    BuildFailedException, ValidationException,
)

__all__ = [
    "CoordSearchContextException",
    
# ========================= NULL COORD_SEARCH_CONTEXT EXCEPTIONS =========================#
    "NullCoordSearchContextException",
    
# ========================= COORD_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
    "InvalidCoordSearchContextException",
    "NoCoordSearchOptionSelectedException",
    "MoreThanOneCoordSearchOptionPickedException",
    
# ========================= COORD_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
    "CoordSearchContextBuildFailedException",
]


class CoordSearchContextException(ContextException):
    """
    Super class of exceptions raised by CoordSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CoordSearchContext raised an exception."


#========================= NULL COORD_SEARCH_CONTEXT EXCEPTIONS =========================#
class NullCoordSearchContextException(CoordSearchContextException, NullException):
    """Raised if an entity, method, or operation requires Coord but gets validation instead."""
    ERROR_CODE = "NULL_COORD_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CoordSearchContext cannot be validation"


#========================= COORD_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
class InvalidCoordSearchContextException(CoordSearchContextException, ValidationException):
    """Catchall Exception for CoordSearchContextValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "COORD_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CoordSearchContext validation failed."


class NoCoordSearchOptionSelectedException(CoordSearchContextException, NoBuildOptionSelectedException):
    """"""
    ERROR_CODE = "NO_COORD_SEARCH_OPTION_SELECTED_ERROR"
    DEFAULT_MESSAGE = "None of the CoordSearchContext options wre selected. An option must be picked."


class MoreThanOneCoordSearchOptionPickedException(
    CoordSearchContextException,
    BuildOptionSelectionTooLargeException
):
    """"""
    ERROR_CODE = "TOO_MANY_COORD_SEARCH_OPTIONS_ERROR"
    DEFAULT_MESSAGE = "Only one CoordSearchContext option can be selected."


#========================= COORD_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
class CoordSearchContextBuildFailedException(CoordSearchContextException, BuildFailedException):
    """
    Catchall Exception for CoordSearchContextBuilder when it encounters an error building
    a CoordSearchContext.
    """
    ERROR_CODE = "COORD_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "CoordSearchContext build failed."