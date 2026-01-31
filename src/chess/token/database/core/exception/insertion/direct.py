# src/chess/token/database/core/exception/insertion/direct.py

"""
Module: chess.token.database.core.exception.insertion.direct
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
    1.  Indicate that appending the occupant directly into self.bag was not in the list after running bag.append.

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
    DEFAULT_MESSAGE = "Token insertion failed: The occupant was not found in self.bag after running self.bag.append."