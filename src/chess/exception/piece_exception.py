from chess.exception.chess_exception import ChessException

"""
Super class for Piece exceptions
"""
class PieceException(ChessException):
    """
    Super class for exceptions raised by Piece objects
    """

    ERROR_CODE = "PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece raised an exception"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"





class KingCheckStateException(PieceException):
    """
    This really should not be an exception. Its really supposed to be a warning to the king
    when its in check. This exception should never be thrown but its messages can be handy.
    """

    ERROR_CODE = "KING_CHECK_STATE"
    DEFAULT_MESSAGE = "A dead piece cannot attack"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


class KingCheckMateStateException(PieceException):
    """
    This really should not be an exception. Its really supposed to be a warning to indicate the
    game is over because the king is checkmated. This exception should never be thrown but its
    messages can be handy.
    """

    ERROR_CODE = "KING_CHECKMATE_STATE"
    DEFAULT_MESSAGE = "King checkmated"

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return f"[{self.ERROR_CODE}] {self.message}"


