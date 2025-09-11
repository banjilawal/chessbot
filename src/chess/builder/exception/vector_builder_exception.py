
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
