__all__ = [
    # ======================# UNHANDLED_BOARD_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "BoardContextValidationRouteException",
]

from chess.board import BoardException
from chess.system import UnhandledRouteException


# ======================# UNHANDLED_BOARD_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class BoardContextValidationRouteException(BoardException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the BoardContext validation failed because there was no build route for the BoardContext key.

    # PARENT:
        *   BoardException
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