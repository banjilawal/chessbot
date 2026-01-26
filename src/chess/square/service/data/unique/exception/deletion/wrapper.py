# src/chess/square/service/data/unique/exception/deletion/wrapper.py

"""
Module: chess.square.service.data.unique.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# DELETING_OCCUPANT_BY_SEARCH_FAILURE EXCEPTION #======================#
    "DeleteTokenBySearchFailedException",
]

from chess.square import SquareException
from chess.system import DeletionFailedException


# ======================# DELETING_OCCUPANT_BY_SEARCH_FAILURE EXCEPTION #======================#
class DeleteTokenBySearchFailedException(SquareException, DeletionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why deleting all occurrences of a square failed. deletion fails. The
        encapsulated exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   SquareException
        *   DeletionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DELETING_OCCUPANT_BY_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "Deleting a token by square failed."