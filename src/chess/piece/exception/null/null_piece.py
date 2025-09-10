from chess.exception.null.base import NullException


class NullPieceException(NullException):
    """
    Raised if a piece is null. Parent class for:
        - NullCombatantPieceException
        - NullKingException
    Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
    Do not throw NullPieceException. Use a finegrained subclass of NullPieceException.
    """

    ERROR_CODE = "NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = f"Piece cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"











