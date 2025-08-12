from chess.exception.null import NullException


class IdNullException(NullException):
    default_message = f"Id {NullException.default_message}"