
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