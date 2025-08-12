from chess.exception.null.null import NullException


class NullNameException(NullException):
    default_message = f"Name {NullException.default_message}"