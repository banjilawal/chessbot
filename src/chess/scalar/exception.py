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

class NullScalarException(ScalarException, NullException):
    """Raised if an required Scalar is null."""
    ERROR_CODE = "NULL_SCALAR_ERROR"
    DEFAULT_MESSAGE = f"Scalar cannot be null"


class ScalarValidationException(ScalarException, ValidationException):
    ERROR_CODE = "SCALAR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Scalar validation failed"


class ScalarBuilderException(ScalarException, BuilderException):
    """Wrapper for exceptions raised when ScalarBuilder runs."""
    ERROR_CODE = "SCALAR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ScalarBuilder raised an exception"


class NullScalarBuilderException(ScalarException, NullException):
    """Raised if a ScalarBuilder is null."""
    ERROR_CODE = "NULL_SCALAR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ScalarBuilder cannot be null"


class ScalarBelowBoundsException(ScalarException):
    """Raised if a scalar is below its < -KNIGHT_STEP_SIZE"""
    ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
    DEFAULT_MESSAGE = "Scalar cannot be less than -KNIGHT_STEP_SIZE"


class ScalarAboveBoundsException(ScalarException):
    """Raised if a scalar is above its > KNIGHT_STEP_SIZE"""
    ERROR_CODE = "SCALAR_UPPER_BOUND_ERROR"
    DEFAULT_MESSAGE = "Scalar cannot be greater than KNIGHT_STEP_SIZE"
