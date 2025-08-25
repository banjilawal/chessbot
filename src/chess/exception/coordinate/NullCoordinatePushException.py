from chess.exception.coordinate.coordinate_exception import CoordinateException


class NullCoordinatePushException(CoordinateException):
    ERROR_CODE = "NULL_COORDINATE_PUSH_STACK_ERROR"
    DEFAULT_MESSAGE = "Cannot push a null coordinate onto the stack"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"