# chess/event/occupation/__init__.py

"""
Module: `chess.event.occupation`
Author: Banji Lawal
Created: 2025-10-01
Updated: 2025-10-02
Version: 1.0.1

# Purpose
Manages `Piece` movement and state changes on the `Board`. Provides a unified interface for event creation, validation,
execution, and rollback for occupation-related operations (move, scan, attack, exchange)

# EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
    - `OccupationEvent`
    - `OccupationTransaction`
    - `OccupationEventValidator`
    - `OccupationEventBuilder`
    - All exceptions from `exception`, `scan`, `attack`, and `exchange` sub-packages.

# SUB-PACKAGES
    - `.exception`: Defines all custom exceptions for occupation operations.
    - `.scan`: Logic for recording occupied squares in a piece's path.
    - `.attack`: Logic for capturing.
    - `.exchange`: Logic for transferring a piece to another empty square.

# NOTES
DO NOT reference sub-modules directly. Import all core classes and exceptions
from this package level (e.g., `from chess.event.occupation import OccupationEvent`).

USAGE:
    # >>> from chess.enemy import CombatantPiece, KingPiece, CoordStack
    # >>> white_pawn_9 = CombatantPiece(discovery_id=9, name="WP1", validation=pawn, team=white_team)
    # >>> white_king = KingPiece(discovery_id=2, name="WK", validation=king, team=white_team)
    # >>>

## Occupation Exception Classes

PURPOSE:
    Contains all exceptions related to enemy operations and state.Contains exceptions raised when a Piece object is
    null or improperly referenced during chess operations.

EXCEPTIONS:
    DoubleCoordPushException: Move to current position
    EncounteringSelfException: Piece encounters itself
    DoublePromotionException: Multiple promotion attempts
    PrisonerEscapeException: Captured enemy tries to move
    PrisonerReleaseException: Error releasing prisoner
    PieceCoordNullException: Piece coordinate is null
    SetCaptorNullException: Setting null captor
    PieceValidationException:raised if PieceValidation fails
    NullPieceException: Abstract base class for null enemy exceptions.
    NullHostagePieceException: Raised when a team tries to add a null hostage enemy to its roster.
    NullCombatantPieceException: Raised when a team tries to remove a captured member but the captor is null.
    NullKingPieceException: Raised when a king enemy reference is null.


USAGE:
    # >>> from chess.enemy.team_exception import PieceCoordNullException
    # >>> from chess.enemy.team_exception.null import NullPieceException
    #
    # >>> if enemy.current_position is None:
    # >>>     raise PieceCoordNullException("Piece coordinate is null")
    # >>> from chess.enemy.team_exception.null import NullPieceException
    # >>> raise NullPieceException(f"{NullPieceException.DEFAULT_MESSAGE}")
___

"""

from .exception import *

from .scan import *
from .attack import *
from .exchange import *
from .event import OccupationEvent
from .builder import OccupationEventBuilder
from .validator import OccupationEventValidator
from .executor import OccupationTransaction

# from .exception import *
# from chess.event.occupation.attack.attack_exceptions import *
#
# from .event import *
# from .executor import OccupationTransaction
# from .validator import OccupationEventValidator

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.transaction.occupation"


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'OccupationEvent',
    'OccupationEventBuilder',
    'OccupationTransaction',
    'OccupationEventValidator',

    # Exception classes
    *exception.__all__,
    *scan.__all__,
    *attack.__all__,
    *exchange.__all__,


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