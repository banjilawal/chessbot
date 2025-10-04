
__all__ = [
    'ChessException',
# === ROLL_BACK EXCEPTIONS ===
    'RollbackException',

# === INCONSISTENCY EXCEPTIONS ===
    'InconsistencyException',
    'InconsistentCollectionException',

# === NULL/EMPTY EXCEPTIONS ===
    'NullException',
    'NullNumberException',
    'NullStringException',
    'BlankStringException'
]

class ChessException(Exception):
    """
    Super class for application exceptions. do not use directly
    """
    ERROR_CODE = "CHESS_ERROR"
    DEFAULT_MESSAGE = "Chess error occurred"

    # Only the super class needs the explict constructor
    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    # Only the super class needs to declare a toString. Subclasses
    # will use this.
    def __str__(self):
        return f"{self.message}"


# === ROLL_BACK EXCEPTIONS ===
class RollbackException(ChessException):
    """
    Base class for rollback-related errors in the chess engine..
    """
    DEFAULT_CODE = "ROLLBACK"
    DEFAULT_MESSAGE = "Operation rolled back due to failure in update consistency."

class RollbackFailedException(RollbackException):
   ERROR_CODE = "ROLLBACK_FAILED_ERROR"
   DEFAULT_MESSAGE = "Rollback failed."


# === INCONSISTENCY EXCEPTIONS ===
class InconsistencyException(ChessException):
    """
    Raised if a data inconsistency is detected
    """
    ERROR_CODE = "DATA_INCONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "A data inconsistency was detected"


class InconsistentCollectionException(InconsistencyException):
    """
    Raised if a collection's state is inconsistent or its data corrupted
    """
    ERROR_CODE = "INCONSISTENT_COLLECTION_ERROR"
    DEFAULT_MESSAGE = (
        "Collection is an inconsistent state. Data might be corrupted"
    )


# === NULL/EMPTY EXCEPTIONS ===
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

class BlankStringException(ChessException):
    """
    Raised if search parameter is a blank or empty string
    """

    ERROR_CODE = "BLANK_SEARCH_STRING_ERROR"
    DEFAULT_MESSAGE = f"Cannot search by an empty or blank string"














