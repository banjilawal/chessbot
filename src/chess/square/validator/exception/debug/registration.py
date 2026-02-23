from chess.square import SquareDebugException, SquareException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# SQUARE_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
    "SquareNotSubmittedBoardRegistrationException",
]


# ======================# SQUARE_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
class SquareNotSubmittedBoardRegistrationException(SquareDebugException, NotRegisteredException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failure ValidationResult was returned because the candidate square had not registered with its board.

    # PARENT:
        *   SquareDebugException
        *   NotRegisteredException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_NOT_REGISTERED_WITH_BOARD_ERROR"
    DEFAULT_MESSAGE = "Square validation failed: The candidate square had not registered with its board."