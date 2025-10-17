# src/chess.coord.exception.py

"""
Module: chess.coord.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **exception classes** that are specific to the
creation, validation, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected domain** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` domain.
It abstracts underlying Python exceptions into domain-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""


from chess.system import EventException, NullException, BuildFailedException, ValidationException, ResourceException, \
  InconsistencyException

#
# __all__ = [
#   'TeamException',
#   'TeamRollBackException',
#
# #====================== TEAM VALIDATION EXCEPTIONS #======================#  
#   'NullTeamException',
#   'InvalidTeamException',
#
#
#
#   'TeamBuildFailedException',
#   'NullTeamSchemaException',
#
# #====================== TEAM MEMBER EXCEPTIONS #======================#  
#   'TeamRosterException',
#   'AddTeamMemberException',
#   'AddEnemyToRosterException',
#   'RemoveTeamMemberException',
#   'FullRankQuotaException',
#
# #====================== TEAM MEMBER EXCEPTIONS WITH ROLLBACK #======================#  
#   'TeamRosterRollBackException',
#   'AddEnemyHostageRolledBackException',
#   'AddTeamMemberRolledBackException',
#   'RemoveTeamMemberRolledBackException',
#   'FullRankQuotaRolledBackException',
#
# #====================== HOSTAGE EXCEPTIONS #======================#  
#   'TeamHostageListException',
#   'InvalidFriendlyHostageException',
#   'AddEnemyHostageException',
#   'AddEnemyKingHostageException',
#   'HostageRemovalException',
#
# #====================== HOSTAGE EXCEPTIONS WITH ROLLBACK #======================#  
#   'TeamHostageListRolledBackException',
#   'InvalidFriendlyHostageRolledBackException',
#   'AddEnemyToRosterRolledBackException',
#   'EnemyKingHostageRolledBackException',
#   'HostageRemovalRolledBackException',
#
# #====================== SEARCH EXCEPTIONS #======================#  
#   'RosterNumberOutOfBoundsException'
# ]

__all__ = [
  'TravelEventException',

#====================== TravelEvent VALIDATION EXCEPTIONS #======================#
  'InvalidTravelEventException',
  'NullTravelEventException',
  'TravelEventActorNotFoundException',
  'EventActorSquareNotFoundException',
  'TravelEventResourceNotFoundException',

#====================== TravelEvent BUILD EXCEPTIONS #======================#
  'TravelEventBuildFailedException',

# ====================== TRAVEL_ACTOR MOVE EXCEPTIONS #======================#
  'TravelActorMovingException',
  'ActorNotOnRosterCannotMoveException',
  'ActorNotOnBoardCannotMoveException',
  'CapturedActorCannotMoveException',
  'AutoTravelPieceException',
]



class TravelEventException(EventException):
  ERROR_CODE = "TRAVEL_EXECUTION_ERROR"
  DEFAULT_MESSAGE = "TravelEvent raised an exception."

#====================== TravelEvent VALIDATION EXCEPTIONS #======================#
class NullTravelEventException(TravelEventException, NullException):
  ERROR_CODE = "NULL_TRAVEL_EXECUTION_ERROR"
  DEFAULT_MESSAGE = "TravelEvent cannot be null."

class InvalidTravelEventException(TravelEventException, ValidationException):
  ERROR_CODE = "TRAVEL_EVENT_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "TravelEvent failed validate"


class TravelEventResourceNotFoundException(TravelEventException, ResourceException):
  ERROR_CODE = "TRAVEL_EVENT_RESOURCE_NOT_FOUND_ERROR"
  DEFAULT_MESSAGE = (
    "TravelEvent resource (the destination_square) was not found during the board_candidate search."
  )

class AutoTravelPieceException(TravelEventException):
  ERROR_CODE = "AUTO_TRAVEL_ERROR"
  DEFAULT_MESSAGE = (
    "Piece is already at the destination. Cannot travel to a square you are already occupying"
  )


#====================== TravelEvent BUILD EXCEPTIONS #======================#
class TravelEventBuildFailedException(TravelEventException, BuildFailedException):
  """
  Indicates TravelEvent could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "TRAVEL_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "TravelEvent build failed."

class OccupationEventBuildFailedException(TravelEventBuildFailedException):
  """
  Indicates OccupationEvent could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "OCCUPATION_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "OccupationEvent build failed."



#
#
#
# class HostageValidationEventException(TravelEventException):
#   ERROR_CODE = "HOSTAGE_VALIDATION_ERROR"
#   DEFAULT_MESSAGE = f"Hostage validation failed."
#
#
# class NullHostagePieceEventException(TravelEventException):
#   """
#   Raised if team enemy is null. Parent class for:
#     - NullCombatantPieceException
#     - NullKingException
#   Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
#   Do not throw NullPieceException. Use team finegrained subclass of NullPieceException.
#   """
#
#   ERROR_CODE = "NULL_PIECE_ERROR"
#   DEFAULT_MESSAGE = f"Piece cannot be null"
#
#
# class NullCombatantPieceEventException(TravelEventException):
#   """
#   Raised if team CombatantPiece is null. Raise NullCombatant instead of NullPieceException
#   """
#
#   ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
#   DEFAULT_MESSAGE = f"CombatantPiece cannot be null"
#
#
# class TravelSearchEventException(TravelEventException):
#   """
#   Board searches during an event should not fai. If they do there is an inconsistency in the board_candidate
#   """
#
#   ERROR_CODE = "TRAVEL_SEARCH_ERROR"
#   DEFAULT_MESSAGE = f"BoardSearch failed to find team square; this should not happen in an event operation"