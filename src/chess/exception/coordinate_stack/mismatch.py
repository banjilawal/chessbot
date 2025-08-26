
from chess.exception.coordinate_stack.coord_stack import CoordinateStackException


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



