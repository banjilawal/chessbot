from chess.exception import ChessException, NullException

__all__ = [
    'BuilderException',
    'NullBuilderException'
]


class BuilderException(ChessException):
    """
    Exceptions raised by chess.creator.builder classes have system behavior. Similar conditions might raise
    exceptions when building entities. During builds ValidatorExceptions are likely. Exceptions thrown during
    entity builds should be wrapped in the BuilderException corresponding to the Builder's name.
    """
    ERROR_CODE = "BUILDER_ERROR"
    DEFAULT_MESSAGE = "Builder  raised an exception"

class NullBuilderException(BuilderException, NullException):
    """
    Methods and classes that do not accept null parameters will raise a NullBuilderException.
    Every class in the application should have a NullBuilderException. Giving each class a unique null
    helps trace errors and failures.

    Attributes:
        message (str): A message describing the team_exception is required.

        Static Fields:
            ERROR_CODE (str): Error code useful in log tracing
            DEFAULT_MESSAGE (Str): Short explanation of why the team_exception was raised
    """
    ERROR_CODE = "NULL_ERROR"
    DEFAULT_MESSAGE = "cannot be null"


class RollbackException(ChessException):
    """
    Base class for rollback-related errors in the chess engine.

    PURPOSE:
        Raised when an transaction (piece move, capture, board update, etc.)
        is reverted due to inconsistency or failed validation.

    ATTRIBUTES:
        code (str): Short machine-readable error code for logging / testing.
        message (str): Human-readable default message.
    """
    DEFAULT_CODE = "ROLLBACK"
    DEFAULT_MESSAGE = "Operation rolled back due to failure in update consistency."


class SearchException(ChessException):
    """
    Base class for search errors in the chess engine.

    PURPOSE:
        Raised search raises an exception. Is a wrapper for other exceptions
        that occur during search.
    ATTRIBUTES:
        code (str): Short machine-readable error code for logging / testing.
        message (str): Human-readable default message.
    """
    DEFAULT_CODE = "SEARCH_ERROR"
    DEFAULT_MESSAGE = "An error was raised during a search."



