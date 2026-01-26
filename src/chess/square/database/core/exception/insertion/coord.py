# src/chess/square/database/core/exception/insertion/coord.py

"""
Module: chess.square.database.core.core.exception.insertion.coord
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_COORD_COLLISION EXCEPTION #======================#
    "SquareCoordCollisionException",
]

from chess.system import CollisionException
from chess.board import BoardSquareServiceException



# ======================# SQUARE_COORD_COLLISION EXCEPTION #======================#
class SquareCoordCollisionException(BoardSquareServiceException, CollisionException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that inserting a square failed because its coord has been assigned to a collection member.

    # PARENT:
        *   CollisionException*
        *   BoardSquareServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_ALREADY_ON_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Adding board square failed: The coord was already referencing the Coord."