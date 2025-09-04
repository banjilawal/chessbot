from chess.exception.null.base import NullException


class NullVectorException(NullException):
    """
    Raised if a vector is null.
    """

    ERROR_CODE = "NULL_VECTOR_ERROR"
    DEFAULT_MESSAGE = f"Vector cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class NullXDimensionException(NullVectorException):
    """
    Raised if a vector's x dimension is null
    """

    ERROR_CODE = "VECTOR_NULL_X_DIMENSION_ERROR"
    DEFAULT_MESSAGE = f"Vector's X-dimension cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class NullYDimension(NullVectorException):
    """
    Raised if a vector's y dimension is null
    """

    ERROR_CODE = "VECTOR_NULL_Y_DIMENSION_ERROR"
    DEFAULT_MESSAGE = f"Vector's Y-dimension cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"