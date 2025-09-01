from chess.exception.stack import StackException


class CoordinateStackException(StackException):
    ERROR_CODE = "COORDINATE_STACK_ERROR"
    DEFAULT_MESSAGE = f"CoordinateStack state threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class InconsistentCurrentCoordinateException(CoordinateStackException):
    ERROR_CODE = "CURRENT_COORDINATE_STATE_ERROR"
    DEFAULT_MESSAGE = "CoordinateStack's current coordinate is in an inconsistent state"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class EmptyStackCurrentCoordinateValueMismatch(CoordinateStackException):
    ERROR_CODE = "EMPTY_STACK_CURRENT_COORDINATE_VALUE_MISMATCH_ERROR"
    DEFAULT_MESSAGE = (
        f"There is a mismatch between the empty state of "
        f"the stack and the current coordinate value."
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

