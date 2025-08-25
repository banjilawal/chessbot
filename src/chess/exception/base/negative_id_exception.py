from chess.exception.base.root import ChessException


class NegativeIdException(ChessException):
    ERROR_CODE = "ID_IS_NEGATIVE"
    DEFAULT_MESSAGE = "Id cannot be negative"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
