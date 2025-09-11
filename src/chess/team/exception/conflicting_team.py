

class ConflictingTeamException(TeamException):
    """
    If a piece that's already on one team (piece.team == not None) tries joining
    another ConflictingTeamException is raised.
    """

    ERROR_CODE = "CONFLICTING_SIDE_ERROR"
    DEFAULT_MESSAGE = "piece is on a different team. Cannot join this one"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


