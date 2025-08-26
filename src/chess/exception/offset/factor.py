
from chess.exception.offset.base import CoordinateOffsetException


class MultiplierOutOfBoundsException(CoordinateOffsetException):
    ERROR_CODE = "OFFSET_FACTOR_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Offset multiplication factor is outside the chessboard range of 1 to 7 inclusive."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



