from chess.exception.null import NullException


class NullNameException(NullException):
    default_message = f"Name {NullException.default_message}"