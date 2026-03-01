# src/logic/coord/database/core/exception/stack/empty.py

"""
Module: logic.coord.database.core.exception.stack.empty
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from logic.coord import CoordStackException

__all__ = [
    # ======================# POPPING_EMPTY_COORD_STACK EXCEPTION #======================#
    "PoppingEmtpyCoordStackException",
]


# ======================# POPPING_EMPTY_COORD_STACK EXCEPTION #======================#
class PoppingEmtpyCoordStackException(CoordStackException):
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
    ERR_CODE = "POPPING_EMPTY_COORD_STACK_EXCEPTION"
    MSG = "Coord deletion failed: CoordStack does not own any coords."