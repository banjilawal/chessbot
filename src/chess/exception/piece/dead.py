from chess.exception.piece.base import PieceException


class DeadPieceMovingException(PieceException):
    ERROR_CODE = "DEAD_PIECE_MOVING_ERROR"
    DEFAULT_MESSAGE = "A dead piece cannot move"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class DeadPieceAttackingException(PieceException):
    ERROR_CODE = "DEAD_PIECE_ATTACKING_ERROR"
    DEFAULT_MESSAGE = "A dead piece cannot attack"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class DuplicateKillException(PieceException):
    ERROR_CODE = "KILLING_DEAD_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot kill a piece already dead"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"