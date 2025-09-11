class ScalarBelowBoundsException(ScalarException):
    ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
    DEFAULT_MESSAGE = f"Scalar is below lower bound"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
