# src/chess/owner/travel/attack/transaction/exception.py

"""
Module: chess.owner.travel.attack.transaction.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import RollbackException
from chess.piece import TravelTransactionException

__all__ = [
  'AttackTransactionException',
  'FailedSettingActorAsEnemyCaptorRolledBackException',
  'FailedEnemyRemovalFromSquareRolledBackException',
  'FailedHostageAdditionRolledBackException',
  'FailedRemovalFromRosterRolledBackException',
  'FailedCapturedPiecFromBoardRolledBackException',
  'FailedRemovalFromBoardRolledBackException'
]

"""
=============================================================================================================#
=======================TRANSACTION EXCEPTIONS ARE ALWAYS ROLL_BACK_EXCEPTION SUBCLASSES======================#
=============================================================================================================#
"""

# ======================# ROLLED BACK ATTACK TRANSACTION EXCEPTIONS #======================#
class AttackTransactionException(TravelTransactionException):
  """
  RollBackCapture exceptions should be raised in ACID transactions where team capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERROR_CODE = "ATTACK_TRANSACTION_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "AttackTransaction raised an rollback_exception. Transaction rolled back."


class RolledBackAttackTransactionException(AttackTransactionException, RollbackException):
  """
  RollBackCapture exceptions should be raised in ACID transactions where team capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERROR_CODE = "ATTACK_TRANSACTION_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "AttackTransaction raised an rollback_exception. Transaction rolled back."

class FailedSettingActorAsEnemyCaptorRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_CAPTOR_PROPERTY_UPDATE_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Updating a prisoner's captor consistency during an attack transaction failed. The transaction was rolled back "
    "before raising this exception."
  )

class FailedEnemyRemovalFromSquareRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_PRISONER_REMOVAL_FROM_SQUARE_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Removing a captured enemy from its square failed during an attack transaction. The transaction was "
    "rolled back before raising this exception."
  )

class FailedHostageAdditionRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_HOSTAGE_ADDITION_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Adding a hostage failed during an attack transaction. The transaction was rolled back before raising this "
    "exception."
  )

class FailedRemovalFromRosterRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_CAPTIVE_REMOVAL_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Removing a captured owner from the team roster failed during an attack transaction. The transaction was rolled "
    "back before raising this exception."
  )

class FailedCapturedPiecFromBoardRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_CAPTURED_PIEC_FROM_BOARD_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Removing a captured owner from the board failed during an attack notification. The notification was rolled back "
    "before this rollback_exception was raised."
  )


class FailedRemovalFromBoardRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_PIECE_REMOVAL_FROM_BOARD_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Removing a captured owner from the board failed during an attack transaction. The transaction was rolled "
    "back before raising this exception."
  )
