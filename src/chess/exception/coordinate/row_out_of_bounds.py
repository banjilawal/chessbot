from chess.common.config import ROW_SIZE
from chess.exception.coordinate.coordinate import CoordinateException


class RowOutOfBoundsException(CoordinateException):
    default_message = (
        f"The coordinate row is outside ChessBoard's row range of 0 to {ROW_SIZE - 1} inclusive."
    )

    def __init__(self, message=default_message):
        self.message = message
        super().__init__(self.message)