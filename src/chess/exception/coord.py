from chess.common.config import COLUMN_SIZE, ROW_SIZE
from chess.exception.base import ChessException

class CoordinateException(ChessException):
    ERROR_CODE = "COORDINATE_ERROR"
    DEFAULT_MESSAGE = f"Invalid Coordinate state threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class RowOutOfBoundsException(CoordinateException):
    ERROR_CODE = "ROW_OUT_OF_BOUNDS"
    DEFAULT_MESSAGE = (
        f"The coordinate row is outside ChessBoard's row range of 0 to {ROW_SIZE - 1} inclusive."
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class ColumnOutOfBoundsException(CoordinateException):
    ERROR_CODE = "COLUMN_OUT_OF_BOUNDS"
    DEFAULT_MESSAGE = (
        f"The coordinate colum is outside ChessBoard's row range of 0 to {COLUMN_SIZE - 1}"
        f" inclusive."
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



