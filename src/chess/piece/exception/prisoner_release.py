class PrisonerReleaseException(PieceException):
    """
    Combatant.captor field can only be set once. PrisonerReleaseException is thrown when an attempt to change
    combatant_piece.captor != null to combatant_piece.captor = None
    """

    ERROR_CODE = "RELEASING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot change CombatantPiece.captor to null once it has been set to an enemy piece"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"