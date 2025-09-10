from chess.exception.chess_exception import ChessException





class ScalarBelowLowerBoundException(ScalarException):
    ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
    DEFAULT_MESSAGE = f"Scalar is below lower bound"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"





class ZeroScalarException(ScalarException):
    ERROR_CODE = "ZERO_SCALAR_ERROR"
    DEFAULT_MESSAGE = f"Scalar cannot be zero."

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"