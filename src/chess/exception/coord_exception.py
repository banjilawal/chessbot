from chess.common.config import COLUMN_SIZE, ROW_SIZE
from chess.exception.chess_exception import ChessException

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
    ERROR_CODE = "COORD_ERROR"
    DEFAULT_MESSAGE = f"Invalid Coord state threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"
















