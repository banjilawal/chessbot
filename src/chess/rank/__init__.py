"""
Rank Package - Contains chess piece movement rank classes.
Each rank defines how a specific chess piece type moves.
"""
from .rank import Rank
from .bishop_rank import Bishop
from .rook_rank import Rook  # Note: Usually called "Rook" in chess
from .king_rank import King
from .knight_rank import Knight
from .pawn_rank import Pawn
from .queen_rank import Queen
from .promoted_rank import PromotedQueen

# Optional: Import common base class if you have one
# try:
#     from .piece_rank import PieceRank  # If you have a base class
# except ImportError:
#     pass

__all__ = [
    'Rank',
    'Bishop',
    'Rook',  # Or 'Rook' if you prefer standard naming
    'King',
    'Knight',
    'Pawn',
    'Queen'
]

# Optional: Convenience dictionary for rank lookup by name
RANK_BY_NAME = {
    'bishop': Bishop,
    'rook': Rook,  # or 'rook'
    'king': King,
    'knight': Knight,
    'pawn': Pawn,
    'queen': Queen
}

# Optional: Utility function to get rank by piece name
def get_rank_by_name(piece_name: str):
    """Get the appropriate rank class for a piece name."""
    name_lower = piece_name.lower()
    for key, rank_class in RANK_BY_NAME.items():
        if key in name_lower:
            return rank_class
    raise ValueError(f"No rank found for piece: {piece_name}")

# Optional: Add to __all__ if you add these utilities
# __all__ = ['Bishop', 'Rook', 'King', 'Knight', 'Pawn', 'Queen', 'get_rank_by_name']