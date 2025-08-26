from chess.exception.null.base import NullException


class XComponentNullException(NullException):
    ERROR_CODE = "VECTOR_X_COMPONENT_NULL_ERROR"
    DEFAULT_MESSAGE = f"X component of vector cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"