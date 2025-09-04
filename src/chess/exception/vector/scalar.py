from chess.exception.vector import VectorException


class ScalarBelowLowerBoundException(VectorException):
    ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
    DEFAULT_MESSAGE = f"Scalar is below lower bound"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ScalarAboveUpperBoundException(VectorException):
    ERROR_CODE = "SCALAR_UPPER_BOUND_ERROR"
    DEFAULT_MESSAGE = f"Scalar is above upper bound"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



class ZeroScalarException(VectorException):
    ERROR_CODE = "ZERO_SCALAR_ERROR"
    DEFAULT_MESSAGE = f"Scalar cannot be zero."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"