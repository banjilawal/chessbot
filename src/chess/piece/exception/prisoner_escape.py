class PrisonerEscapeException(PieceException):
    """
    Combatant pieces with attacker field not null cannot be moved. Attempts to move
    a captured hostage raises PrisonerEscapeException. This only applies to hostage pieces
    """

    ERROR_CODE = "MOVING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot move a captured piece"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"