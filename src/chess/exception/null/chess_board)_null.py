from chess.exception.null.null import NullException


class NullChessBoardException(NullException):
    default_message = f"ChessBoard {NullException.default_message}"