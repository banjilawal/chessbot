from chess.exception import ChessException, BuilderException, NullException, ValidationException

__all__ = [
    'SquareException',

# === SQUARE VALIDATION EXCEPTIONS ===
    'NullSquareException',
    'InvalidSquareException',

# === SQUARE BUILD EXCEPTIONS ===
    'SquareBuildFailed'
]

class SquareException(ChessException):
    """
    Super class of all exceptions a Square object raises. Do not use directly. Subclasses 
    give details useful for debugging. This class exists primarily to allow catching all 
    square exceptions.
    """
    ERROR_CODE = "SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square raised an exception."


# === SQUARE VALIDATION EXCEPTIONS ===
class NullSquareException(SquareException, NullException):
    """Raised if an entity, method, or operation requires a Square but gets null instead."""
    ERROR_CODE = "NULL_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square cannot be null."

class InvalidSquareException(SquareException, ValidationException):
    """
    Raised by SquareValidator if square fails sanity checks. Exists primarily to catch 
    all exceptions raised validating an existing square
    """
    ERROR_CODE = "SQUARE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Square validate failed"

    
# === SQUARE BUILD EXCEPTIONS ===
class SquareBuildFailed(SquareException, BuilderException):
    """
    Raised when SquareBuilder encounters an error building a square. Exists primarily
    to catch all exceptions raised creating a new square
    """
    ERROR_CODE = "SQUARE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Square build failed."
