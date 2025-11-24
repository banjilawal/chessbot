
from chess.piece import PieceException


class KingPieceException(PieceException):
    ERROR_CODE = "KING_PIECE_ERROR"
    DEFAULT_MESSAGE = "KingPiece raised an exception."