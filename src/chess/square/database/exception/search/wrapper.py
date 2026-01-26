# src/chess/square/database/core/exception/search/wrapper.py

"""
Module: chess.square.database.core.exception.search.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_SQUARE_SEARCH_FAILURE EXCEPTION #======================#
    "UniqueSquareSearchFailedException",
]

from chess.square import SquareException
from chess.system import SearchFailedException


# ======================# UNIQUE_SQUARE_SEARCH_FAILURE EXCEPTION #======================#
class UniqueSquareSearchFailedException(SquareException, SearchFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why inserting a unique square failed. The encapsulated exceptions create 
        chain for tracing the source of the failure.

    # PARENT:
        *   SquareException
        *   SearchFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_SQUARE_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Unique square search failed."