from chess.exception.chess_exception import ChessException


class ChessPieceSquareBindingException(ChessException):
    """Exception raised when an id is negative"""
    default_message = " chess-square relationship binding failed"