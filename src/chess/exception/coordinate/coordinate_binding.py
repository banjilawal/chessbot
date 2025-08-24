
from chess.exception.null.null import NullException


class CoordinateBindingException(NullException):
    default_message = "Binding ChessPiece and Square to Coordinate failed"