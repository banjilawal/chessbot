from chess.common.config import COLUMN_SIZE
from chess.exception.coordinate.coordinate import CoordinateException


class ColumnOutOfBoundsException(CoordinateException):
    default_message = (
        f"The coordinate colum is outside ChessBoard's row range of 0 to {COLUMN_SIZE - 1}"
        f" inclusive."
    )