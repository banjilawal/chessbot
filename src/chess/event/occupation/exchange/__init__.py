# chess/event/occupation/exchange__init__.py

"""
Module: `chess.event.occupation.exchange`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

PURPOSE:
    Manages `Piece` movement on the `Board`. After a `Piece.rank` authorizes traveling to a `Square`
    `Rank.walk` initiates an `OccupationEvent`. The package provides a system interface for handling
        - Safe event creation
        - Event validate
        - Event execution
        - Rolling back events
        - Defining exceptions organic to `Event` instances.

##CORE CLASSES:
* `OccupationDirective`
* `OccupationDirectiveValidator`
* `OccupationExecutor`


## USAGE


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

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *
from .event import TransferEvent
from .builder import TransferEventBuilder
from .transaction import TransferTransaction
from .validator import TransferEventValidator



# Package metadata (organic to __init__.py)
__version__ = "1.0.0"
__author__ = "Banji Lawal"
__package_name__ = "chess.event.occupation.exchange"


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'TransferEvent',

    # Exception classes
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