
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
