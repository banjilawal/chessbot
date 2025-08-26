from chess.exception.coordinate_stack.coord_stack import CoordinateStackException


class DuplicateCoordinatePushException(CoordinateStackException):
    ERROR_CODE = "DUPLICATE_COORDINATE_PUSH_STACK_ERROR"
    DEFAULT_MESSAGE = "Cannot push duplicate coordinate onto stack"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"