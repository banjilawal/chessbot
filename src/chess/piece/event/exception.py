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
#   'FailedHostageAdditionRolledBackException',
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
    "TravelEvent resource (the destination_square) was not found during the board_validator search."
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
  Indicates OccupationEventValidator could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "OCCUPATION_EVENT_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "OccupationEventValidator build failed."

class PieceException(ChessException):
  """
  Super class of all exceptions team Piece object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all piece exceptions
  """
  ERROR_CODE = "PIECE_ERROR"
  DEFAULT_MESSAGE = "Piece raised an exception."

class PieceRollBackException(PieceException, RollbackException):
  """
  Any inconsistencies team piece introduces into team transaction need to be rolled back.
  This is the super class of team piece mutator operations, methods, or fields that raise
  errors. Do not use directly. Subclasses give details useful for debugging. This class
  exists primarily to allow catching all Piece exceptions that happen when team failed
  transaction must be rolled back.
  """
  ERROR_CODE = "PIECE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Piece raised an exception."




#======================# NULL PIECE EXCEPTIONS #======================#
class NullPieceException(PieceException, NullException):
  """
  Raised if an entity, method, or operation requires team piece but gets null instead.
  Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
  Do not throw NullAttackException. Raise NullKingPiece or NullCombatantPiece instead.
  they are more descriptive and better suited for debugging.
  """
  ERROR_CODE = "NULL_PIECE_ERROR"
  DEFAULT_MESSAGE = "Piece cannot be null."

class NullKingException(NullPieceException):
  """
  Raised if team KingPiece is null. Raise NullCombatant instead of NullAttackException
  """
  ERROR_CODE = "NULL_KING_PIECE_ERROR"
  DEFAULT_MESSAGE = "KingPiece cannot be null."

class AttackNullCombatantException(NullPieceException):
  """
  Raised if team CombatantPiece is null. Raise NullCombatant instead of NullAttackException
  """
  ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
  DEFAULT_MESSAGE = "CombatantPiece cannot be null."



#======================# PIECE PROMOTION EXCEPTIONS #======================#
class DoublePromotionException(PieceException):
  """
  Raised when attempting promoting team piece already elevated to Queen rank.
  Only pieces with Pawn or King rank can be promoted.
  """
  ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
  DEFAULT_MESSAGE = "Piece is already promoted to Queen. It cannot be promoted again."

class DoublePromotionRolledBackException(PieceRollBackException):
  """
  Raised if team transaction attempts promoting team piece already elevated to Queen rank.
  Only pieces with Pawn or King rank can be promoted. The transaction was rolled
  back before raising this err.
  """
  ERROR_CODE = "DOUBLE_PROMOTION_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Piece is already promoted to Queen. It cannot be promoted again. Transaction "
    "rollback performed."
  )


#======================# PIECE CAPTURE EXCEPTIONS #======================#
class CapturePieceException(PieceException):
  """
  Several exceptions can be raised during capture operations. This class is the parent of
  exceptions team piece can raise being captured or attacking. Do not use directly. Subclasses
  give details useful for debugging.
  """
  ERROR_CODE = "PIECE_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Piece capture attempt raised and err"

class PieceAttackingFriendException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_FRIEND_ERROR"
  DEFAULT_MESSAGE = "Piece cannot attack a friend."

class PieceAttackingKingException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_KING_ERROR"
  DEFAULT_MESSAGE = "Piece cannot attack a king."

class PieceAttackingHostageException(AttackEventException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_HOSTAGE_ERROR"
  DEFAULT_MESSAGE = "Piece cannot attack a hostage."

class AttackingNullException(AttackEventException, NullException):
  """"""
  ERROR_CODE = "PIECE_ATTACKING_NULL_ERROR"
  DEFAULT_MESSAGE = "Piece cannot attack something null."

class HostageCannotAttackException(AttackEventException):
  """
  Raised if team captured piece tries to attack.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Captured piece cannot attack."



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
#   Do not throw NullAttackException. Use team finegrained subclass of NullAttackException.
#   """
#
#   ERROR_CODE = "NULL_PIECE_ERROR"
#   DEFAULT_MESSAGE = f"Piece cannot be null"
#
#
# class NullCombatantPieceEventException(TravelEventException):
#   """
#   Raised if team CombatantPiece is null. Raise NullCombatant instead of NullAttackException
#   """
#
#   ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
#   DEFAULT_MESSAGE = f"CombatantPiece cannot be null"
#
#
# class TravelSearchEventException(TravelEventException):
#   """
#   Board searches during an event should not fai. If they do there is an inconsistency in the board_validator
#   """
#
#   ERROR_CODE = "TRAVEL_SEARCH_ERROR"
#   DEFAULT_MESSAGE = f"BoardSearch failed to find team square; this should not happen in an event operation"