from chess.exception import ChessException, BuilderException, NullException, ValidationException

__all__ = [
    'SquareException',

    # === SQUARE VALIDATION EXCEPTIONS ===
    'NullSquareException',
    'InvalidSquareException',

    # === SQUARE BUILDER EXCEPTIONS ===
    'SquareBuilderException'
]

class SquareException(ChessException):
    """
    Super class of all exceptions a Vector object raises. Do not use directly. Subclasses give details useful 
    for debugging. This class exists primarily to allow catching all vector exceptions
    """
    ERROR_CODE = "SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square raised an exception"


# === SQUARE VALIDATION EXCEPTIONS ===
class NullSquareException(SquareException, NullException):
    """Raised if an entity, method, or operation requires a Square but gets null instead."""
    ERROR_CODE = "NULL_SQUARE_ERROR"
    DEFAULT_MESSAGE = f"Square cannot be null"

class InvalidSquareException(SquareException, ValidationException):
    """
    Raised by VectorValidator if square fails sanity checks. Exists primarily to catch all exceptions raised
    validating an existing vector
    """
    ERROR_CODE = "SQUARE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Square validation failed"

    
# === SQUARE BUILDER EXCEPTIONS ===
class SquareBuilderException(SquareException, BuilderException):
    """
    Raised when VectorBuilder encounters an error while building a vector. Exists primarily to catch all exceptions
    raised building a new vector
    """
    ERROR_CODE = "SQUARE_BUILDER_ERROR"
    DEFAULT_MESSAGE = "SquareBuilder raised an exception"
