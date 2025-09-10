"""
Token Package - Chess Token Data Objects

PURPOSE:
    Contains core chess piece classes and coordinate utilities.
    Provides the fundamental data structures for game pieces.

CORE CLASSES:
    Piece: Abstract base class for all chess pieces
    CombatantPiece: Concrete piece that can be captured
    KingPiece: Concrete king piece with special rules
    CoordStack: Coordinate history and management utility

CONVENIENCE ALIASES:
    BasePiece: Alias for Piece abstract class
    Combatant: Alias for CombatantPiece (shorter, cleaner)
    King: Alias for KingPiece (more intuitive)
    CoordHistory: Alias for CoordStack (more descriptive)

USAGE:
    >>> from chess.piece import CombatantPiece, KingPiecee, CoordStack
    >>> white_pawn_9 = CombatantPiece(piece_id=9, name="WP1", rank=pawn, team=white_team)
    >>> white_king = KingPiece(piece_id=2, name="WK", rank=king, team=white_team)
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Subpackage imports
from . import exception

# Core package imports
from .piece import Piece
from .combatant_piece import CombatantPiece
from .king_piece import KingPiece
from .coord_stack import CoordStack
from .encounter import Encounter

# Aliases
Positions = CoordStack

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "token_package"

# Optional: Package-level constants
MAX_PIECES_PER_TEAM = 16

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
    "Piece",
    "CombatantPiece",
    "KingPiece",
    "CoordStack",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info",
]