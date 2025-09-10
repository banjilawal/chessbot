from chess.exception.null.base import NullException


class NullScalarException(NullException):
    """
    Raised if an required Scalar is null.
    """

    ERROR_CODE = "NULL_SCALAR_ERROR"
    DEFAULT_MESSAGE = f"Scalar cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"