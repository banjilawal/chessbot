# src/chess/square/database/core/exception/insertion/coord.py

"""
Module: chess.square.database.core.exception.insertion.coord
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# COORD_ALREADY_USED_IN_SQUARE_DATASET EXCEPTION #======================#
    "SquareCoordAlreadyInUseException",
]

from chess.square import SquareStackServiceException


# ======================# COORD_ALREADY_USED_IN_SQUARE_DATASET EXCEPTION #======================#
class SquareCoordAlreadyInUseException(SquareStackServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that inserting a item failed because the coord was already in use by a collection member.

    # PARENT:
        *   SquareStackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_ALREADY_USED_IN_SQUARE_DATASET_ERROR"
    DEFAULT_MESSAGE = "Square insertion failed: Another item is already using the coord."