from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
    'ScalarException',
    'NullScalarException',
    'ScalarBuilderException',
    'NullScalarBuilderException',
    'ScalarValidationException',
    'ScalarBelowBoundsException',
    'ScalarAboveBoundsException'
]

class ScalarException(ChessException):
    ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
    DEFAULT_MESSAGE = f"Scalar is below lower bound"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class NullScalarException(NullException):
    """
    Raised if an required Scalar is null.
    """

    ERROR_CODE = "NULL_SCALAR_ERROR"
    DEFAULT_MESSAGE = f"Scalar cannot be null"


class ScalarBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when ScalarBuilder runs.
    """

    ERROR_CODE = "SCALAR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ScalarBuilder  raised an exception"


class NullScalarBuilderException(NullException):
    """
    Raised if a ScalarBuilder is null.
    """

    ERROR_CODE = "NULL_SCALAR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ScalarBuilder cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ScalarValidationException(ValidationException):
    ERROR_CODE = "SCALAR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Scalar validation failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ScalarBelowBoundsException(ScalarException):
    ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
    DEFAULT_MESSAGE = f"Scalar is below lower bound"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ScalarAboveBoundsException(ScalarException):
    ERROR_CODE = "SCALAR_UPPER_BOUND_ERROR"
    DEFAULT_MESSAGE = f"Scalar is above upper bound"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
