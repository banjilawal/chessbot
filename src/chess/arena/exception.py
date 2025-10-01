from chess.exception.exception import ChessException


class ArenaException(ChessException):
    ERROR_CODE = "ARENA_ERROR"
    DEFAULT_MESSAGE = "Invalid Arena state threw an team_exception"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"