__all__ = [
    # ======================# BOARD_SERVICE_INSERTION_OPERATION_FAILURE #======================#
    "BoardLayoutFailedException",
]

from logic.board import BoardException
from system import InsertionException


# ======================# BOARD_LAYOUT_FAILURE #======================#
class BoardLayoutFailedException(BoardException, InsertionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why laying out tokens on a board failed. The encapsulated
        exceptions create chain for tracing the source of the failure.

    Super Class:
        *   BoardException
        *   InsertionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_SERVICE_INSERTION_OPERATION_FAILURE"
    MSG = "Laying out board failed."