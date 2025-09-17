from chess.exception import ChessException, NullException, ValidationException

class SquareException(ChessException):
    ERROR_CODE = "SQUARE_ERROR"
    DEFAULT_MESSAGE = f"Square exception was raised"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class NullSquareException(NullException):
    """
    Raised if a square is null.
    """

    ERROR_CODE = "NULL_SQUARE_ERROR"
    DEFAULT_MESSAGE = f"Square cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class SquareValidationException(ValidationException):
    ERROR_CODE = "SQUARE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Square validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"