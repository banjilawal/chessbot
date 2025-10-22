# src/chess/piece/validation.py

"""
Module: chess.piece.validation.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.piece import PieceException
from chess.system import InconsistencyException, ValidationException, NullException

__all__ = [
#======================# PIECE VALIDATION EXCEPTIONS #======================#
  'InvalidPieceException',
  'PieceTeamFieldIsNullException',
  'PieceMissingCoordStackException',
  'UnregisteredTeamMemberException',
  'PieceRosterNumberIsNullException',
  'PieceRankOutOfBoundsException',
  'PieceMissingDiscoveriesException',

#======================# NULL PIECE EXCEPTIONS #======================#  
  'NullPieceException',
  'NullKingException',
  'NullCombatantException',
]

#======================# PIECE VALIDATION EXCEPTIONS #======================#  
class InvalidPieceException(PieceException, ValidationException):
  """Raised by PieceValidators if client fails validation."""
  ERROR_CODE = "PIECE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Piece validation failed."

class PieceTeamFieldIsNullException(PieceException, InconsistencyException):
  """
  Raised if `piece.team` is null. Might indicate a consistency or build problem because `Piece.team` should
  never be null.
  """
  ERROR_CODE = "PIECE_TEAM_FIELD_NULL_ERROR"
  DEFAULT_MESSAGE = "Piece.team field is null. It should never be null. There may be data inconsistency."

class PieceMissingCoordStackException(PieceException, InconsistencyException):
  """
  Raised if `piece.positions` stack does not exist. If the `piece.positions == null there is data inconsistency
  or loss.
  """
  ERROR_CODE = "PIECE_COORD_STACK_MISSING_ERROR"
  DEFAULT_MESSAGE = "Piece.positions list is null. It should never be null. There may be data inconsistency or loss."

class  PieceMissingDiscoveriesException(PieceException, InconsistencyException):
  """
  Raised if `piece.discovery` list does not exist. If the `piece.discoveries == null there is data inconsistency
  or loss.
  """
  ERROR_CODE = "PIECE_DISCOVERY_LIST_MISSING_ERROR"
  DEFAULT_MESSAGE = "Piece.discovery list is null. It should never be null. There may be data inconsistency or loss."

class UnregisteredTeamMemberException(PieceException):
  """Raised if team piece has its team set but the piece is not on the roster."""
  ERROR_CODE = "UNREGISTERED_TEAM_MEMBER_ERROR"
  DEFAULT_MESSAGE = "The piece has assigned itself a team. but is not listed on that team's roster."

class PieceRosterNumberIsNullException(PieceException, NullException):
  """
  Raised a piece's roster number is null. This should never happen. the invariant roster number
  is set during build. If its null during validation there has been data loss or an inconsistency.
  """
  ERROR_CODE = "PIECE_NULL_ROSTER_NUMBER_ERROR"
  DEFAULT_MESSAGE = "A `Piece` object cannot have a null roster number. There may be data inconsistency or loss."

class PieceRankOutOfBoundsException(PieceException, NullException):
  """
  Raised a piece's rank is not a recognized chess rank
  """
  ERROR_CODE = "PIECE_RANK_OUT_OF_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "A `Piece` does not have a recognized chess rank."

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

class NullCombatantException(NullPieceException):
  """
  Raised if team CombatantPiece is null. Raise NullCombatant instead of NullAttackException
  """
  ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
  DEFAULT_MESSAGE = "CombatantPiece cannot be null."