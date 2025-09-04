from chess.exception.base import ChessException


class BuilderException(ChessException):
    ERROR_CODE = "BUILDER_ERROR"
    DEFAULT_MESSAGE = "Builder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class CoordBuilderException(BuilderException):
    ERROR_CODE = "COORD_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CoordBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class SquareBuilderException(BuilderException):
    ERROR_CODE = "COMPETITOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CompetitorBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class VectorBuilderException(BuilderException):
    ERROR_CODE = "VECTOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "VectorBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class ScalarBuilderException(BuilderException):
    ERROR_CODE = "SCALAR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ScalarBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class PieceBuilderException(BuilderException):
    ERROR_CODE = "PIECE_BUILDER_ERROR"
    DEFAULT_MESSAGE = "PieceBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"