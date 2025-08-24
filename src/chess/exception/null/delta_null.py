from chess.exception.null.null import NullException


class NullDeltaException(NullException):
    default_message = f"Delta cannot be null"

    def __init__(self, message=None):
        if message is None:
            message = self.default_message
        super().__init__(message)