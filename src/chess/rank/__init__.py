"""
Rank Package

PURPOSE:
    Piece uses Rank packge to validate its movement

CORE CLASSES:methods
    Bishop: Provides bishop movement validation
    King: Provides king movement validation
    Knight: Provides knight movement validation
    Pawn: Provides pawn movement validation
    Rook: Provides rook movement validation
    Queen: Provides quuen movement validation

USAGE:
    >>>
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from . import exception

from .rank import Rank
from .bishop_rank import Bishop
from .rook_rank import Rook  # Note: Usually called "Rook" in chess
from .king_rank import King
from .knight_rank import Knight
from .pawn_rank import Pawn
from .queen_rank import Queen
from .promoted_rank import PromotedQueen


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "rank_package"


# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "Bishop",
    "Knight",
    "Pawn",
    "Rook",
    "King",
    "Queen",
]