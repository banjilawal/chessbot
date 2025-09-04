from chess.exception.base import ChessException


class BlankNameException(ChessException):
    """
    Name with only white space raises BlankNameException
    """

    ERROR_CODE = "BLANK_NAME_ERROR"
    DEFAULT_MESSAGE = "Name cannot be white space only"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class NameTooShortException(ChessException):
    """
    Name below the minimum length raises NameTooShortException. See documentation or
    chess.common.config for MIN_NAME_LENGTH.
    """

    ERROR_CODE = "SHORT_NAME_ERROR"
    DEFAULT_MESSAGE = "Name is below the minimum length"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



class NameTooLongException(ChessException):
    """
    Name is longer than MAX_NAME_LENGTH raises NameTooLongException. See documentation
    pr chess.common.config for MAX_NAME_LENGTH
    """

    ERROR_CODE = "LONG_NAME_ERROR"
    DEFAULT_MESSAGE = "Name is above the maximum length"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"