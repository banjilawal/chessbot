from chess.exception.null.null import NullException


class NullCoordinateException(NullException):
    default_message = f"Coordinate {NullException.default_message}"