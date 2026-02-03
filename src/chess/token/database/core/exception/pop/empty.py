# src/chess/token/database/core/exception/deletion/empty.py

"""
Module: chess.token.database.core.exception.deletion.empty
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.token import TokenStackException


__all__ = [
    # ======================# POPPING_EMPTY_TOKEN_STACK EXCEPTION #======================#
    "PoppingEmptyTokenStackException",
]

# ======================# POPPING_EMPTY_TOKEN_STACK EXCEPTION #======================#
class PoppingEmptyTokenStackException(TokenStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a occupant failed because the TokenStack was not managing any tokens.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_TOKEN_STACK_ERROR"
    DEFAULT_MESSAGE = "Token deletion failed: TokenStack does not own any tokens."