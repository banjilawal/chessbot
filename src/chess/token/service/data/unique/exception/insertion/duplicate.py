# src/chess/token/service/data/unique/exception/insertion/duplicate.py

"""
Module: chess.token.service.data.unique.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.token import UniqueTokenDataServiceException

__all__ = [
    # ======================# ADDING_DUPLICATE_TOKEN EXCEPTION #======================#
    "AddingDuplicateTokenException",
]


# ======================# ADDING_DUPLICATE_TOKEN EXCEPTION #======================#
class AddingDuplicateTokenException(UniqueTokenDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a token to the UniqueTokenDataService's dataset failed because the token was
        already in the collection

    # PARENT:
        *   UniqueTokenDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_TOKEN_ERROR"
    DEFAULT_MESSAGE = "Unique token insertion failed: The token is already in the collection."