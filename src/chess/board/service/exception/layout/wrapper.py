__all__ = [
    # ======================# BOARD_SERVICE_INSERTION_OPERATION_FAILURE EXCEPTION #======================#
    "BoardLayoutFailedException",
]

from chess.board import BoardException
from chess.system import InsertionFailedException


# ======================# BOARD_LAYOUT_FAILURE EXCEPTION #======================#
class BoardLayoutFailedException(BoardException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why laying out tokens on a board failed. The encapsulated
        exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   BoardException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BOARD_SERVICE_INSERTION_OPERATION_FAILURE"
    DEFAULT_MESSAGE = "Laying out board failed."