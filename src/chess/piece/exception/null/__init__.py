"""
Null Piece Exception Package - Exceptions Raised When Piece Objects are Null

PURPOSE:
    Contains exceptions rasied when a Piee is null


CORE CLASSES:
    NullPieceException: Abstract base class for null piece exceptions
    HullHostagePieceException: Raised when a tesm tries to a add a Null hostage
    NullCombatantPieceException: Raised when a team is trying to remove a captured member but the captor is null
    NullKingException:

CONVENIENCE ALIASES:
    NullPiece: Alias for Piece abstract class
    NullCombatant: Alias for CombatantPiece (shorter, cleaner)
    NullHostage: Alias for KingPiece (more intuitive)

USAGE:
    >>> from chess.piece.exception.null import NullPiece
    >>>
    >>> if piece is None:
    >>>     raise NullKingPieceException(f"{method}: {NullPieceException.DEFAULT_MESSAGE}")
    >>>

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .null_piece import NullPieceException
from .null_hostage import NullHostagePieceException
from .null_king import NullKingPieceException
from .null_combatant import NullCombatantPieceException

NullPiece = NullPieceException
NullHostage = NullHostagePieceException
NullKingPiece = NullKingPieceException
NullCombatant = NullCombatantPieceException


# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "null_piece_pkg"


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
    "NullPieceException",
    "NullKingPieceException",
    "NullHostagePieceException",
    "NullCombatantPieceException",

    # Organic aliases (defined here)
    "NullPiece",
    "NullKingPiece",
    "NullCombatant",
    "NullHostage",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info",
]