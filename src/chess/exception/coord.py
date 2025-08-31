from chess.common.config import COLUMN_SIZE, ROW_SIZE
from chess.exception.base import ChessException

"""
Super class for Coordinate related exceptions
"""
class CoordinateException(ChessException):

    """
    Super class for Coordinate related exceptions.

    Subclasses:
        - RowBelowBoundsException
        - RowAboveBoundsException
        - ColumnBelowBoundsException
        - ColumnAboveBoundsException
    """
    ERROR_CODE = "COORDINATE_ERROR"
    DEFAULT_MESSAGE = f"Invalid Coordinate state threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Raised if a row is below zero. Domain specific alternative to ArrayIndexOutOfBoundsException
"""
class RowBelowBoundsException(CoordinateException):
    ERROR_CODE = "ROW_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = (
        f"The coordinate row is below lower bound of zero"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Raised if a row is equal or greater than ROW_SIZE. Domain specific alternative 
to ArrayIndexOutOfBoundsException
"""
class RowAboveBoundsException(CoordinateException):
    ERROR_CODE = "ROW_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = (
        f"The coordinate row is above upper bound of {ROW_SIZE-1}"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Raised if a column is below zero. Domain specific alternative to ArrayIndexOutOfBoundsException
"""
class ColumnBelowBoundsException(CoordinateException):
    ERROR_CODE = "COLUMN_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = (
        f"The coordinate colum is below lower bound of zero"
        f" inclusive."
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


"""
Raised if a row is equal or greater than ROW_SIZE. Domain specific alternative 
to ArrayIndexOutOfBoundsException
"""
class ColumnAboveBoundsException(CoordinateException):
    ERROR_CODE = "COLUMN_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = (
        f"The coordinate colum is above upped bound {COLUMN_SIZE-1}"
        f" inclusive."
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



