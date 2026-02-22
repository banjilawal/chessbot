# src/chess/square/database/core/exception/search/wrapper.py

"""
Module: chess.square.database.core.exception.search.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_SQUARE_SEARCH_FAILURE #======================#
    "UniqueSquareSearchException",
]

from chess.square import SquareException
from chess.system import SearchException


# ======================# UNIQUE_SQUARE_SEARCH_FAILURE #======================#
class UniqueSquareSearchException(SquareException, SearchException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why inserting a unique item failed. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   SquareException
        *   SearchException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_SQUARE_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Unique item search failed."