from chess.exception.null.null import NullException


class NullCoordinateStackException(NullException):
    default_message = f"CoordinateStack {NullException.default_message}"