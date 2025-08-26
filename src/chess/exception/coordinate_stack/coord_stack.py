from chess.exception.base.root import ChessException


class CoordinateStackException(ChessException):
    ERROR_CODE = "COORDINATE_STACK_ERROR"
    DEFAULT_MESSAGE = f"CoordinateStack state threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"