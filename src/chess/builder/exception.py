from chess.exception import ChessException, NullException

__all__ = [
    'BuilderException',
    'CoordBuilderException',
    'PieceBuilderException',
    'ScalarBuilderException',
    'VectorBuilderException',
    'CommanderBuilderException'
]

class BuilderException(ChessException):
    """
    Exceptions raised by chess.creator.builder classes have common behavior. Similar conditions might raise
    exceptions when building entities. During builds ValidatorExceptions are likely. Exceptions thrown during
    entity builds should be wrapped in the BuilderException corresponding to the Builder's name.
    """
    ERROR_CODE = "BUILDER_ERROR"
    DEFAULT_MESSAGE = "Builder  raised an exception"


class CoordBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when CoordBuilder runs.
    """

    ERROR_CODE = "COORD_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CoordBuilder raised an exception"


class NullCoordBuilderException(NullException):
    """
    Raised if a CoordBuilder is null.
    """

    ERROR_CODE = "NULL_COORD_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CoordBuilder cannot be null"


class PieceBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when PieceBuilder runs.
    """

    ERROR_CODE = "PIECE_BUILDER_ERROR"
    DEFAULT_MESSAGE = "PieceBuilder raised an exception"

class NullPieceBuilderException(NullException):
    """
    Raised if a CoordBuilder is null.
    """

    ERROR_CODE = "NULL_PIECE_BUILDER_ERROR"
    DEFAULT_MESSAGE = "PieceBuilder cannot be null"


class SquareBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when SquareBuilder runs.
    """

    ERROR_CODE = "SQUARE_BUILDER_ERROR"
    DEFAULT_MESSAGE = "SquareBuilder raised an exception"


class NullSquareBuilderException(NullException):
    """
    Raised if a SquareBuilder is null.
    """

    ERROR_CODE = "NULL_SQUARE_BUILDER_ERROR"
    DEFAULT_MESSAGE = "SquareBuilder cannot be null"


class ScalarBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when ScalarBuilder runs.
    """

    ERROR_CODE = "SCALAR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ScalarBuilder  raised an exception"


class NullScalarBuilderException(NullException):
    """
    Raised if a ScalarBuilder is null.
    """

    ERROR_CODE = "NULL_SCALAR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ScalarBuilder cannot be null"


class VectorBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when vectorBuilder runs.
    """

    ERROR_CODE = "VECTOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "VectorBuilder  raised an exception"


class NullVectorBuilderException(NullException):
    """
    Raised if a VectorBuilder is null.
    """

    ERROR_CODE = "NULL_VECTOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "VectorBuilder cannot be null"


class CommanderBuilderException(BuilderException):
    """
    CommanderBuilder exceptions.
    """
    ERROR_CODE = "COMMANDER_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CommanderBuilder raised team_exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class NullCommanderBuilderException(NullException):
    """
    Raised if a CommanderBuilder is null.
    """

    ERROR_CODE = "NULL_COMMANDER_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CommanderBuilder cannot be null"
