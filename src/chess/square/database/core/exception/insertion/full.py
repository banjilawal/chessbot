# src/chess/square/database/core/exception/push/full.py

"""
Module: chess.square.database.core.exception.push.full
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_STACK_SERVICE EXCEPTION #======================#
    "FullSquareStackException",
]

from chess.system import DebugException
from chess.square import SquareServiceException


# ======================# SQUARE_STACK_SERVICE EXCEPTION #======================#
class FullSquareStackException(SquareServiceException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that adding a item to the service failed because the service has reached the limit of
        how many squares it manages. 

    # PARENT:
        *   DebugException
        *   SquareServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "Adding an item to the SquareStack failed: The stack is full."