from chess.exception.chess_exception import ChessException


class MoveException(ChessException):
    default_message = f"Move failed"



class CapturedPieceMoveException(MoveException):
    default_message = f"Cannot move ChessPiece that has been captured by an enemy"