from chess.exception.null import NullException


class NullSquareException(NullException):
    default_message = f"Square {NullException.default_message}"