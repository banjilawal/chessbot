from chess.square import SquareException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# SQUARE_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
    "SquareNotSubmittedBoardRegistrationException",
]


# ======================# SQUARE_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
class SquareNotSubmittedBoardRegistrationException(SquareException, NotRegisteredException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Square certification because it was not found
        in its owner's squares.

    # PARENT:
        *   SquareException
        *   NotRegisteredException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_NOT_REGISTERED_WITH_BOARD_ERROR"
    DEFAULT_MESSAGE = "Square validation failed: The candidate was not found in its board.squares."