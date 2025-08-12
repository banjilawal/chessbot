from chess.exception.move.move import MoveException


class CapturedChessPieceMoveException(MoveException):
    default_message = f"Captured chess piece {MoveException.default_message}"