
from chess.exception.state.base import StateException


class MovableStateException(StateException):
    ERROR_CODE = "MOVABLE_STATE_ERROR"
    DEFAULT_MESSAGE = f"Chess piece is not in movable state"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class AttackerStateException(StateException):
    ERROR_CODE = "ATTACKER_STATE_ERROR"
    DEFAULT_MESSAGE = f"Piece is not in a state to attack enemies"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class CapturableStateException(StateException):
    ERROR_CODE = "CAPTURABLE_STATE_ERROR"
    DEFAULT_MESSAGE = f"Chess piece cannot be captured"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"