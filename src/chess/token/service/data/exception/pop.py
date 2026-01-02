# src/chess/token/service/data/exception/pop.py

"""
Module: chess.token.service.data.exception.pop
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.token import TokenDataServiceException


__all__ = [
    # ======================# POPPING_EMPTY_TOKEN_DATA_SERVICE EXCEPTION #======================#
    "PoppingEmtpyTokenDataServiceException",
]

# ======================# POPPING_EMPTY_TOKEN_DATA_SERVICE EXCEPTION #======================#
class PoppingEmtpyTokenDataServiceException(TokenDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a token failed because the TokenDataService was not managing any tokens.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_TOKEN_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "Token deletion failed: TokenDataService does not own any tokens."