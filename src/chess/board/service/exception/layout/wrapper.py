__all__ = [
    # ======================# BOARD_SERVICE_INSERTION_OPERATION_FAILURE #======================#
    "BoardLayoutFailedException",
]

from chess.board import BoardException
from chess.system import InsertionException


# ======================# BOARD_LAYOUT_FAILURE #======================#
class BoardLayoutFailedException(BoardException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why laying out tokens on a board failed. The encapsulated
        exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   BoardException
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SERVICE_INSERTION_OPERATION_FAILURE"
    DEFAULT_MESSAGE = "Laying out board failed."