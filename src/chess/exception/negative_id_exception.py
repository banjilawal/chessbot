from chess.exception.chess_exception import ChessException


class NegativeIdException(ChessException):
    """Exception raised when an id is negative"""
    default_message = "Id cannot be negative"
