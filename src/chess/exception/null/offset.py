from chess.exception.null.base import NullException


class NullOffsetException(NullException):
    ERROR_CODE = "NULL_OFFSET_ERROR"
    DEFAULT_MESSAGE = f"Offset cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"