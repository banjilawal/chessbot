from chess.exception import ChessException, NullException, ValidationException

__all__ = [
    'NullNameException',
    'LongNameException',
    'ShortNameException',
    'BlankNameException',
    'NameValidationException',
]

class NameValidationException(ValidationException):
    ERROR_CODE = "NAME_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Name Validation failed"

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


class ShortNameException(ChessException):
    """
    Name below the minimum length raises ShortNameException. See documentation or
    chess.common.config for MIN_NAME_LENGTH.
    """

    ERROR_CODE = "SHORT_NAME_ERROR"
    DEFAULT_MESSAGE = "Name is below the minimum length"


class LongNameException(ChessException):
    """
    Name is longer than MAX_NAME_LENGTH raises LongNameException. See documentation
    pr chess.common.config for MAX_NAME_LENGTH
    """

    ERROR_CODE = "LONG_NAME_ERROR"
    DEFAULT_MESSAGE = "Name is above the maximum length"


class NullNameException(NullException):
    """
    Raised if an entity's name is null
    """

    ERROR_CODE = "NULL_NAME_ERROR"
    DEFAULT_MESSAGE = f"Name cannot be null"

