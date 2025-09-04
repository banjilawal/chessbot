from chess.common.config import KNIGHT_STEP_SIZE
from chess.exception.base import ChessException


class VectorException(ChessException):
    """
    Vectors raised on a vector's fields or methods come in this family. Only use VectorException
    as a fallback. Best practice is create exceptions when a vector fields violate domain logic
    or constraints.
    """

    ERROR_CODE = "VECTOR_ERROR"
    DEFAULT_MESSAGE = f"Vector raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class XBelowLowerBoundException(VectorException):
    """
    Iterating across coordinates to examine squares chess pieces can explore their with a step no
    larger than the knight's number of rows o squares covered in a move. If a vector's x value is
    larger than KNIGHT SIZE raise this exception
    """

    ERROR_CODE = "VECTOR_X_DIMENSION_BELOW_MIN_STEP_SIZE"
    DEFAULT_MESSAGE = f"Vector.x <= {-KNIGHT_STEP_SIZE}. An exception has been raiser"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class XBAboveUpperBoundException(VectorException):
    """
    Iterating across coordinates to examine squares chess pieces can explore their with a step no
    larger than the knight's number of rows o squares covered in a move. If a vector's x value is
    larger than KNIGHT SIZE raise this exception
    """

    ERROR_CODE = "VECTOR_X_DIMENSION_ABOVE_MAX_STEP_SIZE"
    DEFAULT_MESSAGE = f"Vector.x > {KNIGHT_STEP_SIZE}. An exception has been raiser"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

class YBelowULowerBoundException(VectorException):
    """
    Iterating across coordinates to examine squares chess pieces can explore their with a step no
    larger than the knight's number of rows o squares covered in a move. If a vector's x value is
    larger than KNIGHT SIZE raise this exception
    """

    ERROR_CODE = "VECTOR_Y_DIMENSION_BELOW_MIN_STEP_SIZE"
    DEFAULT_MESSAGE = f"Vector.y <= {-KNIGHT_STEP_SIZE}. An exception has been raiser"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class YAboveUpperBoundException(VectorException):
    """
    Iterating across coordinates to examine squares chess pieces can explore their with a step no
    larger than the knight's number of rows o squares covered in a move. If a vector's y value is
    larger than KNIGHT SIZE raise this exception
    """

    ERROR_CODE = "VECTOR_Y_DIMENSION_ABOVE_MAX_STEP_SIZE"
    DEFAULT_MESSAGE = f"Vector.x > {KNIGHT_STEP_SIZE}. An exception has been raiser"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
