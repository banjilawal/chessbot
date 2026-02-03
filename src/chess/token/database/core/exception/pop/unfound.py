# src/chess/token/database/core/exception/deletion/unfound.py

"""
Module: chess.token.database.core.exception.deletion.unfound
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.token import TokenStackException

__all__ = [
    # ======================# TOKEN_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
    "TokenDoesNotExistForRemovalException",
]


# ======================# TOKEN_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
class TokenDoesNotExistForRemovalException(TokenStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a occupant by a unique attribute failed because no bag
        matching the property were found in the dataset.

    # PARENT:
        *   TokenStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_DOES_NOT_EXIST_FOR_REMOVAL_ERROR"
    DEFAULT_MESSAGE = "Token deletion failed: The occupant was not found in the dataset. Nothing to remove."