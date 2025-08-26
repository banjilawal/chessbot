from chess.exception.null.base import NullException


class NullColumnOffsetException(NullException):
    ERROR_CODE = "NULL_COLUMN_OFFSET_ERROR"
    DEFAULT_MESSAGE = f"Column offset cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"