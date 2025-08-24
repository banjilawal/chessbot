from chess.exception.null.null import NullException


class NullSquareException(NullException):
    default_message = f"Square cannot be null"

    def __init__(self, message=None):
        if message is None:
            message = self.default_message
        super().__init__(message)