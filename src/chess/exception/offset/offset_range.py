from chess.exception.coordinate.base import CoordinateException


class OffsetRangeException(CoordinateException):
    ERROR_CODE = "OFFSET_RANGE_ERROR"
    DEFAULT_MESSAGE = f"Invalid Offset range threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



