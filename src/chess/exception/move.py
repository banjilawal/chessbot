from chess.exception.base import ChessException


class MoveException(ChessException):
    ERROR_CODE = "MOVE_ERROR"
    default_message = f"Invalid move operation raised an exception"


    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)


    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"





class CapturedPieceMoveException(MoveException):
    default_message = f"Cannot move ChessPiece that has been captured by an enemy"