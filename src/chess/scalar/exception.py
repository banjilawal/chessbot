from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
    'ScalarException',
    
# === SCALAR VALIDATION EXCEPTIONS ===
    'NullScalarException',
    'InvalidScalarException',
    
# === SCALAR BUILDER EXCEPTIONS ===
    'ScalarBuilderException',

# === SCALAR BOUNDS EXCEPTIONS ===
    'ScalarBelowBoundsException',
    'ScalarAboveBoundsException'
]

class ScalarException(ChessException):
    """
    Super class of all exceptions a Scalar object raises. Do not use directly. Subclasses 
    give details useful for debugging. This class exists primarily to allow catching all 
    Scalar exceptions.
    """
    ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
    DEFAULT_MESSAGE = "Scalar is below lower bound"
    

# === SCALAR VALIDATION EXCEPTIONS ===
class NullScalarException(ScalarException, NullException):
    """Raised if an entity, method, or operation requires a scalar but gets null instead."""
    ERROR_CODE = "NULL_SCALAR_ERROR"
    DEFAULT_MESSAGE = "Scalar cannot be null."

class InvalidScalarException(ScalarException, ValidationException):
    """
    Raised by ScalarValidator if Scalar fails sanity checks. Exists primarily to catch all
    exceptions raised validating an existing scalar
    """
    ERROR_CODE = "SCALAR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Scalar validation failed."


# === SCALAR BUILDER EXCEPTIONS ===
class ScalarBuilderException(ScalarException, BuilderException):
    """
    Raised when ScalarBuilder encounters an exception building a scalar. Exists primarily
    to catch all exceptions raised creating a new scalar.
    """
    ERROR_CODE = "SCALAR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ScalarBuilder raised an exception."


# === SCALAR BOUNDS EXCEPTIONS ===
class ScalarBelowBoundsException(ScalarException):
    """Raised if a scalar is below its < -KNIGHT_STEP_SIZE"""
    ERROR_CODE = "SCALAR_LOWER_BOUND_ERROR"
    DEFAULT_MESSAGE = "Scalar cannot be less than -KNIGHT_STEP_SIZE."

class ScalarAboveBoundsException(ScalarException):
    """Raised if a scalar is above its > KNIGHT_STEP_SIZE"""
    ERROR_CODE = "SCALAR_UPPER_BOUND_ERROR"
    DEFAULT_MESSAGE = "Scalar cannot be greater than KNIGHT_STEP_SIZE."
