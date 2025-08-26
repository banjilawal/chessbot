from chess.exception.coordinate.base import CoordinateException


class MultiplyByZeroException(CoordinateException):
    ERROR_CODE = "MULTIPLY_OFFSET_BY_ZERO_ERROR"
    DEFAULT_MESSAGE = f"Offset multiplication factor cannot be zero."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



