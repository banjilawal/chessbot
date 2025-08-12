from chess.exception.null.null import NullException


class NullSquareException(NullException):
    default_message = f"Square {NullException.default_message}"