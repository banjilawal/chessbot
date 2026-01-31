# src/chess/token/database/core/exception/insertion/wrapper.py

"""
Module: chess.token.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_PUSH_FAILURE EXCEPTION #======================#
    "TokenPushFailedException",
]

from chess.token import TokenStackException
from chess.system import InsertionFailedException


# ======================# TOKEN_PUSH_FAILURE EXCEPTION #======================#
class TokenPushFailedException(TokenStackException, InsertionFailedException):
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
    ERROR_CODE = "TOKEN_PUSH_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Pushing token failed."