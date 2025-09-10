class NullVectorException(NullException):
    """
    Raised if a null-pkg is null.
    """

    ERROR_CODE = "NULL_VECTOR_ERROR"
    DEFAULT_MESSAGE = f"Vector cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"





