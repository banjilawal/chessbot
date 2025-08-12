from chess.exception.null import NullException


class NullChessBoardExcepton(NullException):
    default_message = f"ChessBoard {NullException.default_message}"