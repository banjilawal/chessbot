from chess.common.config import KNIGHT_STEP_SIZE
from chess.exception.offset.base import CoordinateOffsetException


class YVectorBelowMinValueException(CoordinateOffsetException):
    ERROR_CODE = "DELTA_COLUMN_BELOW_STEPPING_BOUND_ERROR"
    DEFAULT_MESSAGE = (
        f"Offset.delta_column less than lower KNIGHT_STEP_SIZE "
        f"bound of {-KNIGHT_STEP_SIZE}"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class YVectorAboveMaxValueException(CoordinateOffsetException):
    ERROR_CODE = "DELTA_COLUMN_ABOVE_STEPPING_BOUND_ERROR"
    DEFAULT_MESSAGE = (
        f"Offset.delta_column larger than upper KNIGHT_STEP_SIZE "
        f"bound of {KNIGHT_STEP_SIZE}"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



