# src/chess/system/travel/travel_exception.py

"""
Module: chess.system.travel.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ChessException, BuilderException, RollbackException

__all__ = [
  'PieceException',
  'PieceRollBackException',

#======================# PIECE BUILD EXCEPTIONS #======================#  
  'PieceBuildFailedException',

#======================# PIECE PROMOTION EXCEPTIONS #======================#  
  'DoublePromotionException',
  'DoublePromotionRolledBackException',

#======================# PIECE CAPTURE EXCEPTIONS #======================#  
  'CapturePieceException',
  'CaptureFriendException',
  'KingCaptureException',
  'DoubleCaptureException',
  'UnsetCaptureException',
  'PieceCapturingItSelfException',

#======================# PIECE CAPTURE EXCEPTIONS WITH ROLLBACK #======================#  
  'CaptureRollbackException',
  'CaptureFriendRolledBackExceptionCapture',
  'KingCaptureRolledBackExceptionCapture',
  'DoubleCaptureRolledBackExceptionCapture',
  'UnsetCaptureRolledBackExceptionCapture',
  'CapturingItSelfRolledBackException',

#======================# ATTACKING PIECE EXCEPTIONS #======================#  
  'HostageActivityException',
  'HostageCannotAttackException',
  'HostageCannotMoveException',
  'HostageCannotScanException'
]

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
  
#======================# PIECE BUILD EXCEPTIONS #======================#  
class PieceBuildFailedException(PieceException, BuilderException):
  """
  Indicates Coord could not be built. Wraps and re-raises errors that occurred
  during build.
  """
  ERROR_CODE = "PIECE_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Piece build failed.."

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

class CaptureFriendException(CapturePieceException):
  """
  Raised if team piece attempts to capture team friend.
  """
  ERROR_CODE = "FRIEND_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Cannot capture team friend."

class KingCaptureException(CapturePieceException):
  """
  Raised if team piece attempts to capture an enemy king. Kings can only be checked or
  checkmated.
  """
  ERROR_CODE = "KING_CAPTURE_ERROR"
  DEFAULT_MESSAGE = (
    "An enemy king cannot be captured. It can only be checked or checkmated."
  )

class DoubleCaptureException(CapturePieceException):
  """
  Raised when team piece attempts to capture an enemy combatant that is already team prisoner
  """
  ERROR_CODE = "DOUBLE_CAPTURE_ERROR"
  DEFAULT_MESSAGE = "Cannot capture team piece that is already team prisoner."

class UnsetCaptureException(CapturePieceException):
  """
  If piece.captor is not null. Attempting to change it raises this err
  """
  ERROR_CODE = "UNSET_CAPTOR_ERROR"
  DEFAULT_MESSAGE =(
    "Cannot set team prisoner's captor to null. A captured piece cannot be freed."
  )


class PieceCapturingItSelfException(CapturePieceException):
  """"""
  ERROR_CODE = "PIECE_CAPTURING_IT_SELF_ERROR"
  DEFAULT_MESSAGE = "Piece cannot capture itself."


#======================# PIECE CAPTURE EXCEPTIONS WITH ROLLBACK #======================#  
class CaptureRollbackException(CapturePieceException, RollbackException):
  """
  RollBackCapture exceptions should be raised in ACID transactions where team capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERROR_CODE = "CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "Capture raised an exception. Transaction rolled back."

class CaptureFriendRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team transaction attempts capturing team friend. The transaction
  was rolled back before raising this err.
  """
  ERROR_CODE = "FRIEND_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot capture team friend. Transaction rollback performed."
  )

class KingCaptureRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team transaction attempts capturing an enemy. Kings can only be checked or
  checkmated. The transaction was rolled back before raising this err.
  """
  ERROR_CODE = "KING_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "An enemy king cannot be captured. It can only be checked or checkmated. "
    "Transaction rollback performed."
  )

class DoubleCaptureRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team transaction attempts capturing an enemy combatant that is already
  team prisoner. The transaction was rolled back before raising this err.
  """
  ERROR_CODE = "DOUBLE_CAPTURE_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot capture team piece that is already team prisoner. Transaction "
    "rollback performed."
  )

class UnsetCaptureRolledBackExceptionCapture(CaptureRollbackException):
  """
  Raised if team transaction attempts setting prisoner's captor field null.
  The transaction was rolled back before raising this err.
  """
  ERROR_CODE = "UNSET_CAPTOR_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = (
    "Cannot set team prisoner's captor to null. A captured piece cannot be freed. "
    "Transaction rollback performed."
  )


class CapturingItSelfRolledBackException(CapturePieceException):
  """
  Raised if team transaction attempts to set team piece as its own captor. The transaction was
  rolled back before raising this err.
  """
  ERROR_CODE = "PIECE_CAPTURING_IT_SELF_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = "Piece attempted to capture itself during the transaction. The transaction was rolled back."


#======================# ATTACKING PIECE EXCEPTIONS #======================#  
class HostageActivityException(PieceException):
  """
  Several exceptions can be raised during capture operations. This class is the parent of
  exceptions an attacking piece can raised. Do not use directly. Subclasses give details
  useful for debugging.
  """
  ERROR_CODE = "HOSTAGE_ACTIVITY_ERROR"
  DEFAULT_MESSAGE = "Hostage piece cannot move, blocked, or attack."


class HostageCannotAttackException(HostageActivityException):
  """
  Raised if team captured piece tries to attack.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_ATTACK_ERROR"
  DEFAULT_MESSAGE = "Captured piece cannot attack."

class HostageCannotMoveException(HostageActivityException):
  """
  Raised if team captured piece tries to move.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_MOVE_ERROR"
  DEFAULT_MESSAGE = "Captured piece cannot move."

class HostageCannotScanException(HostageActivityException):
  """
  Raised if team captured piece tries to blocked team square.
  """
  ERROR_CODE = "HOSTAGE_CANNOT_SCAN_ERROR"
  DEFAULT_MESSAGE = "Captured piece cannot blocked team sqaure."


