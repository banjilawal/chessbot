from chess.exception.chess_exception import ChessException

class FailedPieceRemovalException(ChessException):
    ERROR_CODE = "REMOVE_FROM_BOARD_ERROR"
    DEFAULT_MESSAGE = "Removing captured piece from the board failed"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"