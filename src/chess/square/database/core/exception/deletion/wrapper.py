# src/chess/square/database/core/exception/deletion/wrapper.py

"""
Module: chess.square.database.core.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_DELETION_FAILURE #======================#
    "PoppingSquareException",
]

from chess.square import SquareException
from chess.system import DeletionException


# ======================# SQUARE_DELETION_FAILURE #======================#
class PoppingSquareException(SquareException, DeletionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a SquareStack deletion fails. The encapsulated exceptions create
        chain for tracing the source of the failure.

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
    ERROR_CODE = "SQUARE_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Square deletion failed."