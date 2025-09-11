"""
Null Piece Exception Package - Exceptions Raised When Piece Objects Are Null

PURPOSE:
    Contains exceptions raised when a Piece object is null or improperly referenced
    during chess operations.

CORE CLASSES:
    - NullPieceException: Abstract base class for null piece exceptions.
    - NullHostagePieceException: Raised when a team tries to add a null hostage piece to its roster.
    - NullCombatantPieceException: Raised when a team tries to remove a captured member but the captor is null.
    - NullKingPieceException: Raised when a king piece reference is null.

USAGE:
    >>> from chess.piece.exception.null import NullPieceException
    >>> raise NullPieceException(f"{NullPieceException.DEFAULT_MESSAGE}")

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

# Re-export core null piece exceptions
from .null_piece import NullPieceException
from .null_hostage import NullHostagePieceException
from .null_king import NullKingPieceException
from .null_combatant import NullCombatantPieceException
from .null_encounter import NullEncounterException

# Package metadata
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "piece.exception.null"

# Public API
__all__ = [
    # Core exceptions
    "NullPieceException",
    "NullKingPieceException",
    "NullHostagePieceException",
    "NullCombatantPieceException",
    "NullEncounterException",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info",
]

# Utility function
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }
