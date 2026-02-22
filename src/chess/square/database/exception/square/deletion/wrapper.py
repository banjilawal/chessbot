# src/chess/square/database/exception/deletion/wrapper.py

"""
Module: chess.square.database.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# DELETING_OCCUPANT_BY_SEARCH_FAILURE #======================#
    "DeleteTokenBySearchException",
]

from chess.square import SquareException
from chess.system import DeletionException


# ======================# DELETING_OCCUPANT_BY_SEARCH_FAILURE #======================#
class DeleteTokenBySearchException(SquareException, DeletionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why deleting all occurrences of a item failed. deletion fails. The
        encapsulated exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   SquareException
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DELETING_OCCUPANT_BY_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Deleting a token by item failed."