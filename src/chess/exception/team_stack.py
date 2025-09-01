from chess.exception.base import ChessException


class TeamStackException(ChessException):
    ERROR_CODE = "TEAM_STACK_ERROR"
    DEFAULT_MESSAGE = f"TeamStack state threw an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class InconsistentCurrentTeamException(TeamStackException):
    ERROR_CODE = "CURRENT_TEAM_STATE_ERROR"
    DEFAULT_MESSAGE = "TeamStack's current team is in an inconsistent state"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class EmptyStackCurrentTeamValueMismatch(TeamStackException):
    ERROR_CODE = "EMPTY_STACK_CURRENT_TEAM_VALUE_MISMATCH_ERROR"
    DEFAULT_MESSAGE = (
        f"There is a mismatch between the empty state of "
        f"the stack and the current team value."
    )

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"

