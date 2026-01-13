# src/chess/square/service/data/unique/exception/deletion/wrapper.py

"""
Module: chess.square.service.data.unique.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# EXHAUSTIVE_SQUARE_DELETION_FAILURE EXCEPTION #======================#
    "ExhaustiveSquareDeletionFailedException",
]

from chess.square import SquareException
from chess.system import DeletionFailedException


# ======================# EXHAUSTIVE_SQUARE_DELETION_FAILURE EXCEPTION #======================#
class ExhaustiveSquareDeletionFailedException(SquareException, DeletionFailedException):
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
    ERROR_CODE = "EXHAUSTIVE_SQUARE_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Exhaustive square deletion failed."