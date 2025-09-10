class NullKingPieceException(NullPieceException):
    """
    Raised if a KingPiece is null. Raise NullCombatant instead of NullPieceException
    """

    ERROR_CODE = "NULL_KING_PIECE_ERROR"
    DEFAULT_MESSAGE = f"KingPiece cannot be null"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"