# src/chess/occupant/service/data/exception/deletion/empty.py

"""
Module: chess.occupant.service.data.exception.deletion.empty
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.token import TokenDataServiceException


__all__ = [
    # ======================# POPPING_EMPTY_TOKEN_STACK EXCEPTION #======================#
    "PoppingEmptyTokenStackException",
]

# ======================# POPPING_EMPTY_TOKEN_STACK EXCEPTION #======================#
class PoppingEmptyTokenStackException(TokenDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a occupant failed because the TokenDataService was not managing any tokens.

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
    DEFAULT_MESSAGE = "Token deletion failed: TokenDataService does not own any tokens."