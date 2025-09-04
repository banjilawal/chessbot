from chess.common.config import COLUMN_SIZE, ROW_SIZE
from chess.exception.base import ChessException

"""
Super class for Coord related exceptions
"""
class CoordException(ChessException):

    """
    Super class for Coord related exceptions.

    Subclasses:
        - RowBelowBoundsException
        - RowAboveBoundsException
        - ColumnBelowBoundsException
        - ColumnAboveBoundsException
    """
    ERROR_CODE = "COORDINATE_ERROR"
    DEFAULT_MESSAGE = f"Invalid Coord state threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



class RowBelowBoundsException(CoordException):
    """
    If row < 0 RowBelowBoundsException is raised. Domain specific alternative
    to ArrayIndexOutOfBoundsException
    """

    ERROR_CODE = "ROW_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coord.row < 0. This outside the dimension of the board"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class RowAboveBoundsException(CoordException):
    """
    If a row >= ROW_SIZE RowAboveBoundsException is raised.
    """

    ERROR_CODE = "ROW_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coord.row > {ROW_SIZE-1}. This outside the dimension of the board"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ColumnBelowBoundsException(CoordException):
    """
    If Coord.column < 0 ColumnBelowBoundsException is raised.
    """

    ERROR_CODE = "COLUMN_BELOW_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coordinate.column < 0. This outside the dimension of the board"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ColumnAboveBoundsException(CoordException):
    """
    If Coord.column > DIMENSION ColumnAboveBoundsException is raised.
    """

    ERROR_CODE = "COLUMN_ABOVE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = f"Coord.column > {COLUMN_SIZE-1}. This outside the dimension of the board"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



