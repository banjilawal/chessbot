# chess/operation/occupation/__init__.py

"""
PURPOSE:
    Performs operations for occupying a square

CORE CLASSES:
* `OccupationDirective`
* `OccupationDirectiveValidator`
* `OccupationExecutor`


USAGE:
    # >>> from chess.subject import CombatantPiece, KingPiece, CoordStack
    # >>> white_pawn_9 = CombatantPiece(piece_id=9, name="WP1", validation=pawn, team=white_team)
    # >>> white_king = KingPiece(piece_id=2, name="WK", validation=king, team=white_team)
    # >>>

## Occupation Exception Classes

PURPOSE:
    Contains all exceptions related to subject operations and state.Contains exceptions raised when a Piece object is
    null or improperly referenced during chess operations.

EXCEPTIONS:
    AlreadyAtDestinationException: Move to current position
    EncounteringSelfException: Piece encounters itself
    DoublePromotionException: Multiple promotion attempts
    PrisonerEscapeException: Captured subject tries to move
    PrisonerReleaseException: Error releasing prisoner
    PieceCoordNullException: Piece coordinate is null
    SetCaptorNullException: Setting null captor
    PieceValidationException:raised if PieceValidation fails
    NullPieceException: Abstract base class for null subject exceptions.
    NullHostagePieceException: Raised when a team tries to add a null hostage subject to its roster.
    NullCombatantPieceException: Raised when a team tries to remove a captured member but the captor is null.
    NullKingPieceException: Raised when a king subject reference is null.


USAGE:
    # >>> from chess.subject.team_exception import PieceCoordNullException
    # >>> from chess.subject.team_exception.null import NullPieceException
    #
    # >>> if subject.current_position is None:
    # >>>     raise PieceCoordNullException("Piece coordinate is null")
    # >>> from chess.subject.team_exception.null import NullPieceException
    # >>> raise NullPieceException(f"{NullPieceException.DEFAULT_MESSAGE}")

___


VERSION: 1.0.0
AUTHOR: Banji Lawal

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *
from .attack_exceptions import *

from .directive import OccupationDirective
from .executor import OccupationExecutor
from .validator import OccupationDirectiveValidator

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.operation.occupation"


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'OccupationDirective',
    'OccupationExecutor',
    'OccupationDirectiveValidator',

    # Exception classes
    *exception.__all__,

    *attack_exceptions.__all__,


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