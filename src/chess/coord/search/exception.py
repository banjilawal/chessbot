# src/chess/square/search/collision.py

"""
Module: chess.square.search.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""


from chess.system import (
    BuildOptionSelectionTooLargeException, ContextException, NoBuildOptionSelectedException, NullException,
    BuildFailedException, ValidationException,
)

__all__ = [
    "CoordSearchException",
    
# ========================= NULL COORD_SEARCH_CONTEXT EXCEPTIONS =========================#
    "NullCoordSearchException",
    
# ========================= COORD_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
    "InvalidCoordSearchException",
]


class CoordSearchException(ContextException):
    """
    Super class of exceptions raised by CoordSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CoordSearchContext raised an exception."


# ========================= NULL COORD_SEARCH_CONTEXT EXCEPTIONS =========================#
class NullCoordSearchException(CoordSearchException, NullException):
    """Raised if an entity, method, or operation requires Coord but gets validation instead."""
    ERROR_CODE = "NULL_COORD_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CoordSearchContext cannot be validation"


# ========================= COORD_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
class InvalidCoordSearchException(CoordSearchException, ValidationException):
    """Catchall Exception for CoordSearchContextValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "COORD_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CoordSearchContext validation failed."