
from chess.exception.null.base import NullException


class CoordinateBindingException(NullException):

    ERROR_CODE = "COORDINATE_BINDING_ERROR"
    DEFAULT_MESSAGE = "Binding ChessPiece and Square to Coordinate failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"