from chess.common.config import COLUMN_SIZE
from chess.exception.coordinate.coordinate_exception import CoordinateException


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