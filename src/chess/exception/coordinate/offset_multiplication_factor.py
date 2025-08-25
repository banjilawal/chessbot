from chess.exception.coordinate.coordinate_exception import CoordinateException


class OffsetMultiplicationFactorException(CoordinateException):
    ERROR_CODE = "OFFSET_MULTIPLICATION_FACTOR_ERROR"
    DEFAULT_MESSAGE = f"Offset multiplication factor outside board dimension"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



