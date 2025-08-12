from chess.exception.null import NullException


class NullDeltaException(NullException):
    default_message = f"Delta {NullException.default_message}"