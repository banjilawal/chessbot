# src/chess/coord/service/data/exception/stack/push.py

"""
Module: chess.coord.service.data.exception.stack.push
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# PUSHING_COORD_ONTO_STACK_FAILURE EXCEPTION #======================#
    "PushingCoordOntoStackFailedException",
]

from chess.coord import CoordDataServiceException
from chess.system import InsertionFailedException


# ======================# PUSHING_COORD_ONTO_STACK_FAILURE EXCEPTION #======================#
class PushingCoordOntoStackFailedException(CoordDataServiceException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why pushing a Coord onto the stack fails. The encapsulated 
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   CoordException
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