"""
Piece Exception Package - All Piece-Related Exceptions

PURPOSE:
    Contains all exceptions related to piece operations and state.

EXCEPTIONS:
    AlreadyAtDestinationException: Move to current position
    EncounteringSelfException: Piece encounters itself
    DoublePromotionException: Multiple promotion attempts
    PrisonerEscapeException: Captured piece tries to move
    PrisonerReleaseException: Error releasing prisoner
    PieceCoordNullException: Piece coordinate is null
    SetCaptorNullException: Setting null captor
    PieceValidationException:raised if PieceValidation fails

SUBPAKAGES:
    null: Null reference exceptions (NullPieceException, etc.)

USAGE:
    >>> from chess.piece.exception import PieceCoordNullException
    >>> from chess.piece.exception.null import NullPieceException

    >>> if piece.current_position is None:
    >>>     raise PieceCoordNullException("Piece coordinate is null")

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from . import null

# Import other exceptions (not null ones)
from .already_at_destinaiton import AlreadyAtDestinationException
from .self_encounter import EncounteringSelfException
from .double_promotion import DoublePromotionException
from .prisoner_escape import PrisonerEscapeException
from .prisoner_release import PrisonerReleaseException
from .piece_coord_null import PieceCoordNullException
from .set_captor_null import SetCaptorNullException
from .invalid_piece import PieceValidationException


AlreadyAtDestination = AlreadyAtDestinationException
EncounteringSelf = EncounteringSelfException
DoublePromotion = DoublePromotionException
PrisonerEscape = PrisonerEscapeException
PrisonerRelease = PrisonerReleaseException
SetCaptorNull = SetCaptorNullException
InvalidPiece = PieceValidationException


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


# Make null subpackage available without importing its contents
from . import null

__all__ = [
    # Core exceptions
    "AlreadyAtDestinationException",
    "EncounteringSelfException",
    "DoublePromotionException",
    "PrisonerEscapeException",
    "PrisonerReleaseException",
    "PieceCoordNullException",
    "SetCaptorNullException",
    "PieceValidationException",

    # Aliases
    "AlreadyAtDestination",
    "EncounteringSelf",
    "DoublePromotion",
    "PrisonerEscape",
    "PrisonerRelease",
    "SetCaptorNull",

    # Package metadata and utilities
    "__version__",
    "__author__",
    "package_info"
]