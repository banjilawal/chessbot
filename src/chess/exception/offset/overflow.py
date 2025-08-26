from chess.exception.coordinate.base import CoordinateException


class OffsetMultiplicationOverflowException(CoordinateException):
    ERROR_CODE = "OFFSET_MULTIPLICATION_ERROR"
    DEFAULT_MESSAGE = f"Offset scalar multiplication result outside board dimension"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



