
class SquareBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when SquareBuilder runs.
    """

    ERROR_CODE = "COMPETITOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "CommanderBuilder raised exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"