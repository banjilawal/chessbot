# src/chess/square/context/finder/exception/wrapper.py

"""
Module: chess.square.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import SearchException

__all__ = [
    # ======================# SQUARE_SEARCH_FAILURE #======================#
    "SquareSearchException",
]


# ======================# SQUARE_SEARCH_FAILURE #======================#
class SquareSearchException(SearchException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in SquareFinder.find that, prevented SearchResult.success() from being returned.

    # PARENT:
        *   SearchException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Square search failed."
