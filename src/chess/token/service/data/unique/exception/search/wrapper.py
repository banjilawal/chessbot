# src/chess/occupant/service/data/exception/search/wrapper.py

"""
Module: chess.occupant.service.data.exception.search.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_TOKEN_SEARCH_FAILURE EXCEPTION #======================#
    "UniqueTokenSearchFailedException",
]

from chess.token import TokenException
from chess.system import SearchFailedException


# ======================# UNIQUE_TOKEN_SEARCH_FAILURE EXCEPTION #======================#
class UniqueTokenSearchFailedException(TokenException, SearchFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why inserting a unique occupant failed. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   TokenException
        *   SearchFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_TOKEN_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Unique occupant search failed."