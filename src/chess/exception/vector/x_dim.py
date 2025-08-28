from chess.common.config import KNIGHT_STEP_SIZE
from chess.exception.vector.base import VectorException


class XComponentBelowLowerBoundException(VectorException):
    ERROR_CODE = "DELTA_ROW_BELOW_STEPPING_BOUND_ERROR"
    DEFAULT_MESSAGE = (
        f"Offset.delta_row less than lower KNIGHT_STEP_SIZE bound of {-KNIGHT_STEP_SIZE}"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class XComponentAboveUpperBoundException(VectorException):
    ERROR_CODE = "DELTA_ROW_ABOVE_STEPPING_BOUND_ERROR"
    DEFAULT_MESSAGE = (
        f"Offset.delta_row larger than upper KNIGHT_STEP_SIZE bound of {KNIGHT_STEP_SIZE}"
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"



