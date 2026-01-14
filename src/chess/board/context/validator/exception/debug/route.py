# src/chess/board/context/validator/exception/debug/route.py

"""
Module: chess.board.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PERSONA_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "BoardContextValidationRouteException",
]

from chess.board import BoardContextException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_BOARD_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class BoardContextValidationRouteException(BoardContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the BoardContext validation failed because there was no build route for the BoardContext key.

    # PARENT:
        *   BoardContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_BOARD_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "BoardContext validation failed: No validation route was provided for the Board attribute."