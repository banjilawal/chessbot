# src/chess/coord/database/core/exception/stack/duplicate.py

"""
Module: chess.coord.database.core.exception.stack.duplicate
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.coord import CoordDataServiceException

__all__ = [
    # ======================# PUSHING_DUPLICATE_COORD_ONTO_STACK EXCEPTION #======================#
    "DuplicateCoordPushException",
]


# ======================# PUSHING_DUPLICATE_COORD_ONTO_STACK EXCEPTION #======================#
class DuplicateCoordPushException(CoordDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to push a Coord to the top of the stack failed because it was already at the top.

    # PARENT:
        *   TeamDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PUSHING_DUPLICATE_COORD_ONTO_STACK_ERROR"
    DEFAULT_MESSAGE = "CoordStack push failed: Coord already at top of stack."