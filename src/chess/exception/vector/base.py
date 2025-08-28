from chess.exception.base import ChessException


class VectorException(ChessException):
    ERROR_CODE = "VECTOR_ERROR"
    DEFAULT_MESSAGE = f"Vector raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"