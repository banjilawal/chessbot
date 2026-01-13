# src/chess/square/service/data/exception/deletion/wrapper.py

"""
Module: chess.square.service.data.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_DELETION_FAILURE EXCEPTION #======================#
    "SquareDeletionFailedException",
]

from chess.square import SquareException
from chess.system import DeletionFailedException


# ======================# SQUARE_DELETION_FAILURE EXCEPTION #======================#
class SquareDeletionFailedException(SquareException, DeletionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a SquareStack deletion fails. The encapsulated exceptions create
        chain for tracing the source of the failure.

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
    ERROR_CODE = "SQUARE_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Square deletion failed."