from chess.exception.null import NullException


class NullChessPieceException(NullException):
    default_message = f"ChessPiece {NullException.default_message}"