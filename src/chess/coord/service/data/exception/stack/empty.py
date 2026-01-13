# src/chess/coord/service/data/exception/stack/empty.py

"""
Module: chess.coord.service.data.exception.stack.empty
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordDataServiceException

__all__ = [
    # ======================# POPPING_EMPTY_COORD_STACK EXCEPTION #======================#
    "PoppingEmtpyCoordStackException",
]


# ======================# POPPING_EMPTY_COORD_STACK EXCEPTION #======================#
class PoppingEmtpyCoordStackException(CoordDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a coord failed because the stack was empty

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_EMPTY_COORD_STACK_ERROR"
    DEFAULT_MESSAGE = "Coord deletion failed: CoordDataService does not own any coords."