# src/chess/token/service/data/exception/insertion/direct.py

"""
Module: chess.token.service.data.exception.insertion.direct
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# APPENDING_TOKEN_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
    "AppendingTokenDirectlyIntoItemsFailedException",
]

from chess.token import TokenDataServiceException


# ======================# APPENDING_TOKEN_DIRECTLY_INTO_ITEMS EXCEPTION #======================#
class AppendingTokenDirectlyIntoItemsFailedException(TokenDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that appending the token directly into self.items was not in the list after running items.append.

    # PARENT:
        *   TokenDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "APPENDING_TOKEN_DIRECTLY_INTO_ITEMS_ERROR"
    DEFAULT_MESSAGE = "Token insertion failed: The token was not found in self.items after running self.items.append."