class NullCombatantPieceException(NullPieceException):
    """
    Raised if a CombatantPiece is null. Raise NullCombatant instead of NullPieceException
    """

    ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = f"CombatantPiece cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"