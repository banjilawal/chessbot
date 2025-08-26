from chess.exception.coordinate_stack.coordinate_stack_exception import CoordinateStackException


class PopEmptyCoordinateStackException(CoordinateStackException):
    ERROR_CODE = "POP_EMPTY_COORDINATE_STACK_ERROR"
    DEFAULT_MESSAGE = "Cannot pop from empty coordinate stack"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"