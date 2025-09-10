from chess.exception.chess_exception import ChessException


class BuilderException(ChessException):
    """
    Exceptions raised by chess.creator.builder classes have common behavior. Similar conditions might raise
    exceptions when building entities. During builds ValidatorExceptions are likely. Exceptions thrown during
    entity builds should be wrapped in the BuilderException corresponding to the Builder's name.
    """
    ERROR_CODE = "BUILDER_ERROR"
    DEFAULT_MESSAGE = "Builder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class CoordBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when CoordBuilder runs.
    """

    ERROR_CODE = "COORD_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CoordBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class SquareBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when SquareBuilder runs.
    """

    ERROR_CODE = "COMPETITOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CompetitorBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class VectorBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when vectorBuilder runs.
    """

    ERROR_CODE = "VECTOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "VectorBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class ScalarBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when ScalarBuilder runs.
    """

    ERROR_CODE = "SCALAR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ScalarBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class PieceBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when PieceBuilder runs.
    """

    ERROR_CODE = "PIECE_BUILDER_ERROR"
    DEFAULT_MESSAGE = "PieceBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"