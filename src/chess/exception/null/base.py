from chess.exception.base import ChessException


class NullException(ChessException):
    ERROR_CODE = "NULL_ERROR"
    DEFAULT_MESSAGE = "cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"














