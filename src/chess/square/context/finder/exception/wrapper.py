# src/chess/square/context/finder/exception/wrapper.py

"""
Module: chess.square.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import SearchException

__all__ = [
    # ======================# SQUARE_SEARCH_FAILURE #======================#
    "SquareSearchException",
]


# ======================# SQUARE_SEARCH_FAILURE #======================#
class SquareSearchException(SquareException, SearchException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any condition that prevents a search from completing creates a debug exception that explains why the query
        failed. That debug exception is wrapped in the SquareSearchException which is the middle layer of the
        3-part exception chain.

    # PARENT:
        *   SquareException
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
