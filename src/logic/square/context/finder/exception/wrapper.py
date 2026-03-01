# src/logic/square/context/finder/exception/wrapper.py

"""
Module: logic.square.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from logic.system import SearchException

__all__ = [
    # ======================# SQUARE_SEARCH_FAILURE #======================#
    "SquareSearchException",
]


# ======================# SQUARE_SEARCH_FAILURE #======================#
class SquareSearchException(SearchException):
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

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
    ERR_CODE = "SQUARE_SEARCH_FAILURE"
    MSG = "Square search failed."
