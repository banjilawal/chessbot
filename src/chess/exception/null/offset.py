from chess.exception.null.null_exception import NullException


class NullDeltaException(NullException):
    ERROR_CODE = "NULL_DELTA_ERROR"
    DEFAULT_MESSAGE = f"Delta cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"