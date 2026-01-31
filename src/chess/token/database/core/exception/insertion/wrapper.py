# src/chess/token/database/core/exception/insertion/wrapper.py

"""
Module: chess.token.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_INSERTION_FAILURE #======================#
    "TokenInsertionFailedException",
]

from chess.token import TokenException
from chess.system import InsertionFailedException


# ======================# TOKEN_INSERTION_FAILURE #======================#
class TokenInsertionFailedException(TokenException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that add a occupant to the roster failed.

    # PARENT:
        *   TokenException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_INSERTION_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Token insertion failed."