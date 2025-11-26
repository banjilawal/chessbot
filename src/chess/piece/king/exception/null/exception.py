
from chess.system import NullException
from chess.piece import InvalidKingPieceException

__all__ = [
    # ======================# NULL KING EXCEPTIONS #======================#
    "NullKingException",
]

# ======================# NULL KING EXCEPTIONS #======================#
class NullKingException(InvalidKingPieceException, NullException):
    """Raised if an entity, method, or operation expects a KingPiece but gets null instead."""
    ERROR_CODE = "NULL_KING_PIECE_ERROR"
    DEFAULT_MESSAGE = "KingPiece cannot be null."