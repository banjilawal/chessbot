# src/chess/token/database/core/exception/search/wrapper.py

"""
Module: chess.token.database.core.exception.search.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_TOKEN_SEARCH_FAILURE #======================#
    "UniqueTokenSearchException",
]

from chess.token import TokenException
from chess.system import SearchException


# ======================# UNIQUE_TOKEN_SEARCH_FAILURE #======================#
class UniqueTokenSearchException(TokenException, SearchException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why inserting a unique occupant failed. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   TokenException
        *   SearchException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_TOKEN_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Unique occupant search failed."