from chess.exception.invalid_move import MovingException


class KnightMovingException(MovingException):
    ERROR_CODE = "KNIGHT_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid knight move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"