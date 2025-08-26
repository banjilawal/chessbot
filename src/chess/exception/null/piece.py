from chess.exception.null.base import NullException


class NullChessPieceException(NullException):
    ERROR_CODE = "NULL_CHESS_PIECE_ERROR"
    DEFAULT_MESSAGE = f"ChessPiece cannot be null"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"