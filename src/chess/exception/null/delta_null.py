from chess.exception.null.null import NullException


class NullDeltaException(NullException):
    default_message = f"Delta {NullException.default_message}"