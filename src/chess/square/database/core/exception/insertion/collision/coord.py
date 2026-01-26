# src/chess/square/database/core/exception/insertion/coord.py

"""
Module: chess.square.database.core.exception.insertion.coord
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# COORD_ALREADY_USED_IN_SQUARE_DATASET EXCEPTION #======================#
    "CoordAlreadyUsedInSquareDatasetException",
]

from chess.square import SquareDataServiceException


# ======================# COORD_ALREADY_USED_IN_SQUARE_DATASET EXCEPTION #======================#
class CoordAlreadyUsedInSquareDatasetException(SquareDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that inserting a square failed because the coord was already in use by a collection member.

    # PARENT:
        *   SquareDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_ALREADY_USED_IN_SQUARE_DATASET_ERROR"
    DEFAULT_MESSAGE = "Square insertion failed: Another square is already using the coord."