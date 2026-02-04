# src/chess/coord/database/core/exception/stack/push.py

"""
Module: chess.coord.database.core.exception.stack.push
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# PUSHING_COORD_ONTO_STACK_FAILURE EXCEPTION #======================#
    "PushingCoordFailedException",
]


from chess.system import InsertionFailedException


# ======================# PUSHING_COORD_ONTO_STACK_FAILURE EXCEPTION #======================#
class PushingCoordFailedException(CoordStackException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why pushing a Coord onto the stack fails. The encapsulated 
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   CoordStackException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PUSHING_COORD_ONTO_STACK_FAILURE"
    DEFAULT_MESSAGE = "Pushing a Coord onto the stack failed."