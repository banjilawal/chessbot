# src/chess/token/service/data/unique/exception/duplicate.py

"""
Module: chess.token.service.data.unique.exception.duplicate
Author: Banji Lawal
Created: 2025-11-19
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
    1.  Indicate that an attempt to add a token to the UniqueTokeDataService's dataset failed because the token was
        already in the collection

    # PARENT:
        *   UniqueTeamDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_TOKEN_ERROR"
    DEFAULT_MESSAGE = (
        "Token insertion failed: UniqueTokenDataService is already managing the token. It cannot be added to the "
        "dataset again."
    )