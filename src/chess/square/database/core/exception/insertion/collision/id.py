# src/chess/square/database/core/exception/insertion/id.py

"""
Module: chess.square.database.core.exception.insertion.id
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# ID_ALREADY_USED_IN_SQUARE_DATASET EXCEPTION #======================#
    "SquareIdAlreadyInUseException",
]

from chess.square import SquareDataServiceException


# ======================# ID_ALREADY_USED_IN_SQUARE_DATASET EXCEPTION #======================#
class SquareIdAlreadyInUseException(SquareDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that inserting a square failed because the id was already in use by a collection member.

    # PARENT:
        *   SquareDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ID_ALREADY_USED_IN_SQUARE_DATASET_ERROR"
    DEFAULT_MESSAGE = "Square insertion failed: Another square is already using the id."