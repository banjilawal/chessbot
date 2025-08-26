from chess.common.config import KNIGHT_WALKING_RANGE
from chess.exception.coordinate.base import CoordinateException


class ColumnOffsetSizeException(CoordinateException):
    ERROR_CODE = "COLUMN_OFFSET_OUT_OF_BOUNDS"
    DEFAULT_MESSAGE = (
        f"Column offset must be within range "
        f"[{-KNIGHT_WALKING_RANGE}, {KNIGHT_WALKING_RANGE}] "
        f"inclusive"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



