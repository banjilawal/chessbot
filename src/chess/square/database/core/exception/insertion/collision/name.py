# src/chess/square/database/core/exception/insertion/name.py

"""
Module: chess.square.database.core.exception.insertion.name
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# NAME_ALREADY_USED_IN_SQUARE_DATASET EXCEPTION #======================#
    "NameAlreadyUsedInSquareDatasetException",
]

from chess.square import SquareDataServiceException


# ======================# NAME_ALREADY_USED_IN_SQUARE_DATASET EXCEPTION #======================#
class NameAlreadyUsedInSquareDatasetException(SquareDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that inserting a square failed because the name was already in use by a collection member.

    # PARENT:
        *   SquareDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NAME_ALREADY_USED_IN_SQUARE_DATASET_ERROR"
    DEFAULT_MESSAGE = "Square insertion failed: Another square is already using the name."