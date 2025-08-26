from chess.exception.offset.base import CoordinateOffsetException


class NegativeMultiplierException(CoordinateOffsetException):
    ERROR_CODE = "NEGATIVE_OFFSET_MULTIPLICATION_FACTOR_ERROR"
    DEFAULT_MESSAGE = f"Offset multiplication factor cannot be negative."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"