from chess.exception.null.null_exception import NullException


class IdNullException(NullException):
    ERROR_CODE = "NULL_ID_ERROR"
    DEFAULT_MESSAGE = f"Id cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"