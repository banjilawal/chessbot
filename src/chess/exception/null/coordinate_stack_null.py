from chess.exception.null.null_exception import NullException


class NullCoordinateStackException(NullException):
    ERROR_CODE = "NULL_COORDINATESTACK_ERROR"
    DEFAULT_MESSAGE = f"CoordinateStack cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"