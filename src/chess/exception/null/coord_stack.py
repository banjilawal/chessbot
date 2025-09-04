from chess.exception.null.base import NullException


class NullCoordStackException(NullException):
    """
    Raised if a piece's CoordinateStack (Piece.positions) is null.
    """

    ERROR_CODE = "NULL_COORDINATE_STACK_ERROR"
    DEFAULT_MESSAGE = f"CoordinateStack cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"