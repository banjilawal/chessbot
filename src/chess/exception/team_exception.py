from chess.exception.chess_exception import ChessException


class TeamException(ChessException):
    """
    Super class for exception raised by a Team object when its internal fields or methods
    """

    ERROR_CODE = "SIDE_ERROR"
    DEFAULT_MESSAGE = "Team raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

