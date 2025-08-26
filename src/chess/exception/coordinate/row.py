from chess.common.config import ROW_SIZE
from chess.exception.coordinate.coordinate_exception import CoordinateException


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
