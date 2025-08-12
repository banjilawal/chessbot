from chess.exception.exception import ChessException


class NullException(ChessException):
    default_message = "cannot be null"

class IdNullException(NullException):
    default_message = f"Id {NullException.default_message}"

class NullNameException(NullException):
    default_message = f"Name {NullException.default_message}"

class NullCoordinateException(NullException):
    default_message = f"Coordinate {NullException.default_message}"

class NullDeltaException(NullException):
    default_message = f"Delta {NullException.default_message}"

class NullChessPieceException(NullException):
    default_message = f"ChessPiece {NullException.default_message}"

class NullCoordinateStackException(NullException):
    default_message = f"CoordinateStack {NullException.default_message}"

class NullSquareException(NullException):
    default_message = f"Square {NullException.default_message}"

class NullBoardException(NullException):
    default_message = f"Square {NullException.default_message}"