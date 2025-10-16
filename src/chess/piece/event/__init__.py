# chess/piece/event/__init__.py

"""
Module: `chess.piece.event`
Author: Banji Lawal
Created: 2025-10-06
Version: 1.0.1

# Purpose
Manages `Piece` movement and state changes on the `Board`. Provides team unified interface for event creation, validate,
execution, and rollback for event-related operations (move, scan, attack, occupy)

# EXPORTS
This package exposes core classes and all exceptions from its sub-modules:
  - `TravelEvent`
  - `TravelContext`
  - `TravelEventBuilder`
  - `OccupationEventValidator`
  - `OccupationEventBuilder`
  - All exports from `scan`, `attack`, `promote`, and `occupy` packages.
  - All exceptions from `er`, `scan`, `attack`, and `occupy` sub-packages.

# SUB-PACKAGES
  - `.attack`: Logic for capturing.
  - `.promote`: Logic for promoting kings and pawns.
  - `.exception`: Defines all custom exceptions for event operations.
  - `.scan`: Logic for recording occupied squares in team piece's path.
  - `.occupy`: Logic for transferring team piece to another empty square.

# NOTES
DO NOT reference subpackages or submodules directly. Import all subpackages and submodules from the
`piece` level package.

USAGE:
  # >>> from chess.enemy import CombatantPiece, KingPiece, CoordStack
  # >>> white_pawn_9 = CombatantPiece(discovery_id=9, name="WP1", validate=pawn, team=white_team)
  # >>> white_king = KingPiece(discovery_id=2, name="WK", validate=king, team=white_team)
  # >>>

## Occupation Exception Classes

PURPOSE:
  Contains all exceptions related to enemy operations and state.Contains exceptions raised when team Piece object is
  null or improperly referenced during chess operations.

EXCEPTIONS:
  DoubleCoordPushException: Move to current position
  EncounteringSelfException: Piece encounters itself
  DoublePromotionException: Multiple promote attempts
  PrisonerEscapeException: Captured enemy tries to move
  PrisonerReleaseException: Error releasing prisoner
  PieceCoordNullException: Piece coordinate is null
  SetCaptorNullException: Setting null captor
  PieceValidationException:raised if PieceValidation fails
  NullPieceException: Abstract base class for null enemy exceptions.
  NullHostagePieceException: Raised when team team tries to add team null hostage enemy to its roster.
  NullCombatantPieceException: Raised when team team tries to remove team captured member but the captor is null.
  NullKingPieceException: Raised when team king enemy reference is null.


USAGE:
  # >>> from chess.enemy.team_exception import PieceCoordNullException
  # >>> from chess.enemy.team_exception.null import NullPieceException
  #
  # >>> if enemy.current_position is None:
  # >>>   raise PieceCoordNullException("Piece coordinate is null")
  # >>> from chess.enemy.team_exception.null import NullPieceException
  # >>> raise NullPieceException(f"{NullPieceException.DEFAULT_MESSAGE}")
___

"""

from .scan import *
from .attack import *
from .occupy import *
from .promote import *
from .exception import *

from .event import TravelEvent
from .context import TravelContext
from .builder import OccupationEventBuilder
from .transaction import TravelTransaction
from .validator import OccupationEventValidator

# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.piece.event"

# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'TravelEvent',
  'OccupationEventBuilder',
  'TravelTransaction',
  'OccupationEventValidator',

  *scan.__all__,
  *attack.__all__,
  *occupy.__all__,
  *promote.__all__,

  *exception.__all__,

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