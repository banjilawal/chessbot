from chess.exception.move.move import MoveException


class EmptyStackChessPieceMoveException(MoveException):
    default_message = f"Empty stack chess piece {MoveException.default_message}"