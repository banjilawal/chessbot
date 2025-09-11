from chess.exception.invalid_move import MovingException


class KingMovingException(MovingException):
    ERROR_CODE = "KING_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid king move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"