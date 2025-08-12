from chess.exception.null.null import NullException


class NullOwnerException(NullException):
    default_message = f"Owner {NullException.default_message}"