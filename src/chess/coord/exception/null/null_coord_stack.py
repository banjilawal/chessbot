from chess.exception.null_exception import NullException


class NullCoordStackException(NullException):
    """
    Raised if a piece's CoordStack (Piece.positions) is null.
    """

    ERROR_CODE = "NULL_COORD_STACK_ERROR"
    DEFAULT_MESSAGE = f"CoordStack cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"