from chess.exception.base import ChessException

class CoordinateException(ChessException):
    ERROR_CODE = "COORDINATE_ERROR"
    DEFAULT_MESSAGE = f"Invalid Coordinate state threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



