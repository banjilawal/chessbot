from .chess_exception import ChessException

class Square(ChessException):
    ERROR_CODE = "SQUARE_ERROR"
    DEFAULT_MESSAGE = f"Square exception was raised"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"