# src/chess/token/database/exception/push/duplicate.py

"""
Module: chess.token.database.exception.push.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.token import TokenStackException

__all__ = [
    # ======================# ADDING_DUPLICATE_TOKEN EXCEPTION #======================#
    "AddingDuplicateTokenException",
]


# ======================# ADDING_DUPLICATE_TOKEN EXCEPTION #======================#
class AddingDuplicateTokenException(TokenStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing a token onto the stack failed because it was already present in the stack.

    # PARENT:
        *   TokenStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_TOKEN_ERROR"
    DEFAULT_MESSAGE = "Pushing token failed: The token was already present in the stack."