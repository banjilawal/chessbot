from chess.exception.chess_exception import ChessException


class NullException(ChessException):
    """
    Methods and classes that do not accept null parameters will raise a NullException.
    Every class in the application should have a NullException. Giving each class a unique null
    helps trace errors and failures.

    Attributes:
        message (str): A message describing the exception is required.

        Static Fields:
            ERROR_CODE (str): Error code useful in log tracing
            DEFAULT_MESSAGE (Str): Short explanation of why the exception was raised
    """

    ERROR_CODE = "NULL_ERROR"
    DEFAULT_MESSAGE = "cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"














