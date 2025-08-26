from chess.exception.null.base import NullException


class NullTeamException(NullException):
    ERROR_CODE = "NULL_TEAM_ERROR"
    DEFAULT_MESSAGE = f"Team cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"