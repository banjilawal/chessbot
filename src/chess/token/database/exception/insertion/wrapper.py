# src/chess/token/database/core/exception/insertion/wrapper.py

"""
Module: chess.token.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# UNIQUE_TOKEN_INSERTION_FAILURE EXCEPTION #======================#
    "TokenDatabaseInsertionException",
]

from chess.token import TokenException
from chess.system import InsertionFailedException


# ======================# UNIQUE_TOKEN_INSERTION_FAILURE EXCEPTION #======================#
class TokenDatabaseInsertionException(TokenException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why inserting a unique occupant failed. The encapsulated exceptions create
        chain for tracing the source of the failure.

    # PARENT:
        *   TokenException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNIQUE_TOKEN_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Unique occupant insertion failed."