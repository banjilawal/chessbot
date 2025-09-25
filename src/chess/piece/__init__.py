# chess/piece/__init__.py

"""
Piece Package - Chess Piece Data Objects

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
    >>> from chess.piece import CombatantPiece, KingPiece, CoordStack
    >>> white_pawn_9 = CombatantPiece(piece_id=9, name="WP1", validation=pawn, team=white_team)
    >>> white_king = KingPiece(piece_id=2, name="WK", validation=king, team=white_team)
    >>>

Piece Exception Package - All Piece-Related Exceptions

PURPOSE:
    Contains all exceptions related to piece operations and state.Contains exceptions raised when a Piece object is
    null or improperly referenced during chess operations.

EXCEPTIONS:
    AlreadyAtDestinationException: Move to current position
    EncounteringSelfException: Piece encounters itself
    DoublePromotionException: Multiple promotion attempts
    PrisonerEscapeException: Captured piece tries to move
    PrisonerReleaseException: Error releasing prisoner
    PieceCoordNullException: Piece coordinate is null
    SetCaptorNullException: Setting null captor
    PieceValidationException:raised if PieceValidation fails
    NullPieceException: Abstract base class for null piece exceptions.
    NullHostagePieceException: Raised when a team tries to add a null hostage piece to its roster.
    NullCombatantPieceException: Raised when a team tries to remove a captured member but the captor is null.
    NullKingPieceException: Raised when a king piece reference is null.


USAGE:
    >>> from chess.piece.team_exception import PieceCoordNullException
    >>> from chess.piece.team_exception.null import NullPieceException

    >>> if piece.current_position is None:
    >>>     raise PieceCoordNullException("Piece coordinate is null")
    >>> from chess.piece.team_exception.null import NullPieceException
    >>> raise NullPieceException(f"{NullPieceException.DEFAULT_MESSAGE}")

___


VERSION: 1.0.0
AUTHOR: Banji Lawal

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *

from .piece import *
from .encounter import Encounter
from .builder import PieceBuilder
from .validator import PieceValidator
from .encounter_scan import EncounterScan

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "piece"


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    "Piece",
    "CombatantPiece",
    "KingPiece",
    "PieceValidator",
    "Encounter",
    "EncounterScan",
    "PieceBuilder",

    *exception.__all__,

    # Subpackages
    "exception",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info"
]

# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        "name": __package_name__,
        "version": __version__,
        "author": __author__,
        "exports": __all__
    }