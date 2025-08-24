from chess.exception.negative_id_exception import ChessException


class NullException(ChessException):
    default_message = "cannot be null"

    def __init__(self, message=None):
        if message is None:
            message = self.default_message
        super().__init__(message)














