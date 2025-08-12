from chess.exception.null.null import NullException


class IdNullException(NullException):
    default_message = f"Id {NullException.default_message}"