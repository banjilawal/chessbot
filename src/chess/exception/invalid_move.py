
class MovingException(ChessException):
    ERROR_CODE = "_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"