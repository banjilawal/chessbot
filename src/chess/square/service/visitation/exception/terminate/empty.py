# src/chess/square/service/visitation/exception/terminate/empty.py

"""
Module: chess.square.service.visitation.exception.terminate.empty
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_IS_EMPTY EXCEPTION #======================#
    "NoVisitForTerminationException",
]

from chess.square import SquareDebugException


# ======================# SQUARE_IS_EMPTY EXCEPTION #======================#
class NoVisitForTerminationException(SquareDebugException):
      
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that removing a occupant from a item failed because the item was empty.

    # PARENT:
        *   SquareException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_IS_EMPTY_ERROR"
    DEFAULT_MESSAGE = "Removing occupant from item failed: The item was empty. Nothing to remove."