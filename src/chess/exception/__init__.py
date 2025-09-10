"""
Texception Package - Project wide exceptions

PURPOSE:
    Contains core exceptions for entities. .


CORE CLASSES:
    PieceException: Supe class for exceptons raiedby Piece classes
    CombatantPiece: Concrete piece that can be captured
    KingPiece: Concrete king piece with special rules
    CoordStack: Coordinate history and management utility

CONVENIENCE ALIASES:
    BasePiece: Alias for Piece abstract class
    Combatant: Alias for CombatantPiece (shorter, cleaner)
    King: Alias for KingPiece (more intuitive)
    CoordHistory: Alias for CoordStack (more descriptive)

USAGE:
    >>> from chess.piece import CombatantPiece, KingPiecee, CoordHistory
    >>> piece = Combatant(piece_id=1, name="Pawn-A", validation=pawn_rank, team=white_team)
    >>> king = King(piece_id=2, name="White-King", validation=king_rank, team=white_team)
    >>> history = CoordHistory()

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Core package imports

from . import id
from . import name


from .vector_exception import VectorException
from .coord_exception import CoordException
from .rank_exception import RankException
from .board_exception import BoardException
from .vector_exception import VectorException
from .scalar_exception import ScalarException
from .search import SearchException
from .square_exception import SquareException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "exception_package"


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
    "ChessException",
    "CoordException",
    "PieceExeption",
    "BoardException",
    "TeamException",
    "SquareException",
    "NegativeIdException",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info",
]