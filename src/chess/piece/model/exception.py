# src/chess/owner/model/exception.py

"""
Module: chess.owner.model.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import (
  ChessException, BuilderException, InconsistencyException, NullException, ValidationException
)

__all__ = [
  'PieceException',
  
  # ======================# PIECE VALIDATION EXCEPTIONS #======================#
  'InvalidPieceException',
  'PieceTeamFieldIsNullException',
  'PieceMissingCoordStackException',
  'UnregisteredTeamMemberException',
  'PieceRosterNumberIsNullException',
  'PieceRankOutOfBoundsException',
  'PieceMissingDiscoveriesException',
  
  # ======================# NULL PIECE EXCEPTIONS #======================#
  'NullPieceException',
  'NullKingException',
  'NullCombatantException',

#======================# PIECE BUILD EXCEPTIONS #======================#  
  'PieceBuildFailedException',
]

class PieceException(ChessException):
  """
  Super class of all exceptions team Piece object raises. Do not use directly. Subclasses
  give details useful for debugging. This class exists primarily to allow catching
  all owner exceptions
  """
  ERROR_CODE = "PIECE_ERROR"
  DEFAULT_MESSAGE = "Piece raised an rollback_exception."

# ======================# PIECE VALIDATION EXCEPTIONS #======================#
class InvalidPieceException(PieceException, ValidationException):
  """Raised by PieceValidators if client fails validator."""
  ERROR_CODE = "PIECE_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Piece validator failed."


class PieceTeamFieldIsNullException(PieceException, InconsistencyException):
  """
  Raised if `owner.team` is null. Might indicate a consistency or build problem because `Piece.team` should
  never be null.
  """
  ERROR_CODE = "PIECE_TEAM_FIELD_NULL_ERROR"
  DEFAULT_MESSAGE = "Piece.team consistency is null. It should never be null. There may be service inconsistency."


class PieceMissingCoordStackException(PieceException, InconsistencyException):
  """
  Raised if `owner.positions` stack does not exist. If the `owner.positions == null there is service inconsistency
  or loss.
  """
  ERROR_CODE = "PIECE_COORD_STACK_MISSING_ERROR"
  DEFAULT_MESSAGE = "Piece.positions list is null. It should never be null. There may be service inconsistency or loss."


class PieceMissingDiscoveriesException(PieceException, InconsistencyException):
  """
  Raised if `owner.discovery` list does not exist. If the `owner.discoveries == null there is service inconsistency
  or loss.
  """
  ERROR_CODE = "PIECE_DISCOVERY_LIST_MISSING_ERROR"
  DEFAULT_MESSAGE = "Piece.discovery list is null. It should never be null. There may be service inconsistency or loss."


class UnregisteredTeamMemberException(PieceException):
  """Raised if piece has its team set but the owner is not on the roster."""
  ERROR_CODE = "UNREGISTERED_TEAM_MEMBER_ERROR"
  DEFAULT_MESSAGE = "The piece has assigned itself a team. but is not listed on that team's roster."


class PieceRosterNumberIsNullException(PieceException, NullException):
  """
  Raised a owner's roster number is null. This should never happen. the invariant roster number
  is set during build. If its null during validator there has been service loss or an inconsistency.
  """
  ERROR_CODE = "PIECE_NULL_ROSTER_NUMBER_ERROR"
  DEFAULT_MESSAGE = "A `Piece` object cannot have a null roster number. There may be service inconsistency or loss."


class PieceRankOutOfBoundsException(PieceException, NullException):
  """
  Raised a owner's bounds is not a recognized chess bounds
  """
  ERROR_CODE = "PIECE_RANK_OUT_OF_BOUNDS_ERROR"
  DEFAULT_MESSAGE = "A `Piece` does not have a recognized chess bounds."


# ======================# NULL PIECE EXCEPTIONS #======================#
class NullPieceException(PieceException, NullException):
  """
  Raised if an entity, method, or operation requires team owner but gets null instead.
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
  
#======================# PIECE BUILD EXCEPTIONS #======================#  
class PieceBuildFailedException(PieceException, BuilderException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "PIECE_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Piece build failed.."
