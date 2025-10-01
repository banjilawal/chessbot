from chess.exception.exception import ChessException


class TeamHistoryException(ChessException):
    ERROR_CODE = "TEAM_STACK_ERROR"
    DEFAULT_MESSAGE = f"TeamStack state threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class CurrentTeamException(TeamHistoryException):
    ERROR_CODE = "CURRENT_TEAM_STATE_ERROR"
    DEFAULT_MESSAGE = "TeamStack's current team is in an inconsistent state"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

