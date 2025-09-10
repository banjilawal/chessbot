from chess.exception.chess_exception import ChessException
from chess.exception.null.base import NullException


class NullBoardException(NullException):
    """
    If null is passed as a parameter instead of a Board then NullBoardException is raised
    """

    ERROR_CODE = "NULL_BOARD_ERROR"
    DEFAULT_MESSAGE = "Board cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"














