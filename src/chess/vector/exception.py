from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
    'VectorException',

    # === VECTOR VALIDATION EXCEPTIONS ===
    'NullVectorException',
    'InvalidVectorException',

    # === VECTOR BUILDER EXCEPTIONS ===
    'VectorBuilderException',

    # === NULL COMPONENT EXCEPTIONS ===
    'VectorAboveBoundsException',
    'VectorBelowBoundsException',

    # === VECTOR BOUNDS EXCEPTIONS ===
    'NullXComponentException',
    'NullYComponentException',
]

class VectorException(ChessException):
    """
    Super class of all exceptions a Vector object raises. Do not use directly. Subclasses give details useful
    for debugging. This class exists primarily to allow catching all vector exceptions
    """
    ERROR_CODE = "VECTOR_ERROR"
    DEFAULT_MESSAGE = "Vector raised an exception"


# === VECTOR VALIDATION EXCEPTIONS ===
class NullVectorException(VectorException, NullException):
    """Raised if an entity, method, or operation requires a vector but gets null instead."""
    ERROR_CODE = "NULL_VECTOR_ERROR"
    DEFAULT_MESSAGE = f"Vector cannot be null"


class InvalidVectorException(VectorException, ValidationException):
    """
    Raised by VectorValidator if vector fails sanity checks. Exists primarily to catch all exceptions raised
    validating an existing vector
    """
    ERROR_CODE = "VECTOR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Vector validation failed"


# === VECTOR BUILDER EXCEPTIONS ===
class VectorBuilderException(VectorException, BuilderException):
    """
    Raised when VectorBuilder encounters an exception while building a team. Exists primarily to catch all exceptions
    raised build a new vector
    """
    ERROR_CODE = "VECTOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "VectorBuilder raised an exception"


# === NULL COMPONENT EXCEPTIONS ===
class NullXComponentException(VectorException, NullException):
    """Raised if a vector's x dimension is null"""
    ERROR_CODE = "VECTOR_NULL_X_DIMENSION_ERROR"
    DEFAULT_MESSAGE = f"Vector's X-dimension cannot be null"


class NullYComponentException(VectorException, NullException):
    """Raised if a vector's y dimension is null"""
    ERROR_CODE = "VECTOR_NULL_Y_DIMENSION_ERROR"
    DEFAULT_MESSAGE = f"Vector's Y-dimension cannot be null"


# === VECTOR BOUNDS EXCEPTIONS ===
class VectorAboveBoundsException(VectorException):
    """
    Iterating across coordinates to examine squares chess pieces can explore their with a step no
    larger than the knight's number of rows o squares covered in a move. If a vector's x value is
    larger than KNIGHT SIZE raise this exception
    """
    ERROR_CODE = "VECTOR_ABOVE_BOUNDS"
    DEFAULT_MESSAGE = "Vector above bounds"


class VectorBelowBoundsException(VectorException):
    """
    Iterating across coordinates to examine squares chess pieces can explore their with a step no
    larger than the knight's number of rows o squares covered in a move. If a vector's x value is
    larger than KNIGHT SIZE raise this exception
    """
    ERROR_CODE = "VECTOR_BELOW_BOUNDS_EXCEPTION"
    DEFAULT_MESSAGE =  "Vector is below bounds"






