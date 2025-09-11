from chess.exception.stack_exception import StackException


class CoordinateStackException(StackException):
    ERROR_CODE = "COORDINATE_STACK_ERROR"
    DEFAULT_MESSAGE = f"CoordStack state threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class InconsistentCurrentCoordinateException(CoordinateStackException):
    ERROR_CODE = "CURRENT_COORDINATE_STATE_ERROR"
    DEFAULT_MESSAGE = "CoordStack's current coord is in an inconsistent state"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

