from chess.exception.null import NullException


class NullOwnerException(NullException):
    default_message = f"Owner {NullException.default_message}"