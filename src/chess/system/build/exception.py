from chess.exception import ChessException, NullException

__all__ = [
    'BuilderException',
    'NullBuilderException',
    'FailedBuildException'
]


class BuilderException(ChessException):
    """
    Exceptions raised by chess.creator.build classes have system behavior. Similar conditions might raise
    exceptions when building entities. During builds ValidatorExceptions are likely. Exceptions thrown during
    entity builds should be wrapped in the BuilderException corresponding to the Builder's name.
    """
    ERROR_CODE = "BUILDER_ERROR"
    DEFAULT_MESSAGE = "Builder  raised an err"

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
    DEFAULT_MESSAGE = "Builder cannot be null"

class FailedBuildException(BuilderException):
    """
    Raised when PieceBuilder encounters an error while building a team. Exists primarily to
    catch all exceptions raised building a new piece
    """
    ERROR_CODE = "BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = " build failed."



