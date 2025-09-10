class NullYDimensionException(NullVectorException):
    """
    Raised if a null-pkg's y dimension is null
    """

    ERROR_CODE = "VECTOR_NULL_Y_DIMENSION_ERROR"
    DEFAULT_MESSAGE = f"Vector's Y-dimension cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"