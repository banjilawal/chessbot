# src/chess/token/service/data/exception/current.py

"""
Module: chess.token.service.data.exception.current
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.token import TokenDataServiceException

__all__ = [
    # ======================# DUPLICATE_COORD_STACK_PUSH EXCEPTION #======================#
    "DuplicateCoordStackPushException",
]


# ======================# DUPLICATE_COORD_STACK_PUSH EXCEPTION #======================#
class DuplicateCoordStackPushException(TokenDataServiceException):
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
    ERROR_CODE = "DUPLICATE_COORD_STACK_PUSH_ERROR"
    DEFAULT_MESSAGE = "CoordStack push failed: Coord already at top of stack."