from chess.exception.null.null import NullException


class NullChessBoardExcepton(NullException):
    default_message = f"ChessBoard {NullException.default_message}"