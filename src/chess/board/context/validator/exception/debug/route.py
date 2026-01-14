# src/chess/board/context/validator/exception/debug/route.py

"""
Module: chess.board.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import UnhandledRouteException
from chess.board import BoardContextException

__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "BoardContextValidationRouteException",
]


# ======================# UNHANDLED_BOARD_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class BoardContextValidationRouteException(BoardContextException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the BoardContext validation failed because there was no build route for the BoardContext key.

    # PARENT:
        *   ResultException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_BOARD_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "BoardContext validation failed: No validation route was provided for the Board attribute."