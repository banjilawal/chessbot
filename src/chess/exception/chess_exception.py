
__all__ = [
    'ChessException',
    'NullException',
    'IdNullException',
    'IdValidationException',
    'NegativeIdException',
    'NullNameException',
    'LongNameException',
    'ShortNameException',
    'BlankNameException',
    'BlankStringException',
    'NameValidationException',
    'NullStringException',
    'NullNumberException',
    'ValidationException'
]

class ChessException(Exception):
    """
    Top level Exception for the chess application. ChessException is a template for
    other exceptions.

    Exception Requirements:
        - Static fields:
            ERROR_CODE (str): Must end in _ERROR. all caps summary of the team_exception or its cause
            DEFAULT_MESSAGE (str): Short sentence explaining what the team_exception is about.

        - A ChessException should always have a message describing the error.
    """

    ERROR_CODE = "CHESS_ERROR"
    DEFAULT_MESSAGE = "Chess error occurred"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

# === NULL SUPER CLASS EXCEPTION ===

class NullException(ChessException):
    """
    Methods and classes that do not accept null parameters will raise a NullException.
    Every class in the application should have a NullException. Giving each class a unique null
    helps trace errors and failures.

    Attributes:
        message (str): A message describing the team_exception is required.

        Static Fields:
            ERROR_CODE (str): Error code useful in log tracing
            DEFAULT_MESSAGE (Str): Short explanation of why the team_exception was raised
    """
    ERROR_CODE = "NULL_ERROR"
    DEFAULT_MESSAGE = "cannot be null"


# === TOP LEVEL VALIDATION EXCEPTION ===

class ValidationException(ChessException):
    ERROR_CODE = "VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Validation failed"


# === ID RELATED EXCEPTION ===

class IdValidationException(ValidationException):
    ERROR_CODE = "ID_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Id Validation failed"

class IdNullException(NullException):
    """
    Raised if an entity's id is null
    """
    ERROR_CODE = "NULL_ID_ERROR"
    DEFAULT_MESSAGE = f"Id cannot be null"


class NegativeIdException(ChessException):
    ERROR_CODE = "ID_IS_NEGATIVE"
    DEFAULT_MESSAGE = "Id cannot be negative"


# === NAME RELATED EXCEPTIONS ===

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


class BlankStringException(ChessException):
    """
    Raised if search parameter is a blank or empty string
    """

    ERROR_CODE = "BLANK_SEARCH_STRING_ERROR"
    DEFAULT_MESSAGE = f"Cannot search by an empty or blank string"


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


class NullNumberException(NullException):
    """
    Raised if mathematical expression or geometric, algebraic, or optimization that need
     a number but get null instead NUllNumberException is thrown. Ids are not used for math
     so we need a different null team_exception for math variables
    """

    ERROR_CODE = "NULL_NUMBER_ERROR"
    DEFAULT_MESSAGE = f"Number cannot be null"


class NullStringException(NullException):
    """
    Raised if search parameter is a null string
    """

    ERROR_CODE = "NULL_STRING_SEARCH_ERROR"
    DEFAULT_MESSAGE = f"Cannot search by a null string"

