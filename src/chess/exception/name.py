from chess.exception.base import ChessException

"""
Name with only white space raises this exception
"""
class BlankNameException(ChessException):
    ERROR_CODE = "BLANK_NAME_ERROR"
    DEFAULT_MESSAGE = "Name cannot be white space only"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Name is shorter than 3 characters raises this exception.
"""
class NameTooShortException(ChessException):
    ERROR_CODE = "SHORT_NAME_ERROR"
    DEFAULT_MESSAGE = "Name is below the minimum length"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Name is longer than 40 characters this exception is thrown.
"""
class NameTooLongException(ChessException):
    """
    Name is longer than 40 characters this exception is thrown.
    """

    ERROR_CODE = "LONG_NAME_ERROR"
    DEFAULT_MESSAGE = "Name is above the maximum length"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"