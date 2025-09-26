from chess.exception import ChessException, NullException, ValidationException, BuilderException

__all__ = [
    'VectorException',
    'VectorBuilderException',
    'NullVectorBuilderException',
    'NullVectorException',
    'VectorAboveBoundsException',
    'VectorBelowBoundsException',
    'NullXComponentException',
    'NullYComponentException',
    'VectorValidationException'
]

class VectorException(ChessException):
    """
    Vectors raised on a null-pkg's fields or methods come in this family. Only use VectorException
    as a fallback. Best practice is create exceptions when a null-pkg fields violate domain logic
    or constraints.
    """

    ERROR_CODE = "VECTOR_ERROR"
    DEFAULT_MESSAGE = f"Vector raised an team_exception"


class VectorBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when vectorBuilder runs.
    """

    ERROR_CODE = "VECTOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "VectorBuilder  raised an exception"


class NullVectorBuilderException(NullException):
    """
    Raised if a VectorBuilder is null.
    """

    ERROR_CODE = "NULL_VECTOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "VectorBuilder cannot be null"


class VectorValidationException(ValidationException):
    ERROR_CODE = "VECTOR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Vector validation failed"


# === NULL VECTOR EXCEPTIONS ===
class NullVectorException(NullException):
    """
    Raised if a null-pkg is null.
    """

    ERROR_CODE = "NULL_VECTOR_ERROR"
    DEFAULT_MESSAGE = f"Vector cannot be null"


class NullXComponentException(NullException):
    """
    Raised if a null-pkg's x dimension is null
    """

    ERROR_CODE = "VECTOR_NULL_X_DIMENSION_ERROR"
    DEFAULT_MESSAGE = f"Vector's X-dimension cannot be null"


class NullYComponentException(NullException):
    """
    Raised if a null-pkg's y dimension is null
    """

    ERROR_CODE = "VECTOR_NULL_Y_DIMENSION_ERROR"
    DEFAULT_MESSAGE = f"Vector's Y-dimension cannot be null"


# === VECTOR BOUNDS EXCEPTIONS ===
class VectorAboveBoundsException(VectorException):
    """
    Iterating across coordinates to examine squares chess pieces can explore their with a step no
    larger than the knight's number of rows o squares covered in a move. If a null-pkg's x value is
    larger than KNIGHT SIZE raise this team_exception
    """

    ERROR_CODE = "VECTOR_ABOVE_BOUNDS"
    DEFAULT_MESSAGE = f"Vector above bounds"


class VectorBelowBoundsException(VectorException):
    """
    Iterating across coordinates to examine squares chess pieces can explore their with a step no
    larger than the knight's number of rows o squares covered in a move. If a null-pkg's x value is
    larger than KNIGHT SIZE raise this team_exception
    """

    ERROR_CODE = "VECTOR_BELOW_BOUNDS_EXCEPTION"
    DEFAULT_MESSAGE = f"Vector is below bounds"






