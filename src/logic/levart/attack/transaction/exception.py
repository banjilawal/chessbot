# src/logic/owner/travel/attack/transaction/collision.py

"""
Module: logic.owner.travel.attack.transaction.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from logic.system import RollbackException
from logic.piece import TravelTransactionException

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
=======================TRANSACTION EXCEPTION ARE ALWAYS ROLL_BACK_EXCEPTION SUBCLASSES======================#
=============================================================================================================#
"""

#======================# ROLLED BACK ATTACK TRANSACTION EXCEPTION #======================#
class AttackTransactionException(TravelTransactionException):
  """
  RollBackCapture exception should be raised in ACID transactions where team_name capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERR_CODE = "ATTACK_TRANSACTION_EXCEPTION_ROLLED_BACK"
  MSG = "AttackTransaction raised an rollback_exception. Transaction rolled back."


class RolledBackAttackTransactionException(AttackTransactionException, RollbackException):
  """
  RollBackCapture exception should be raised in ACID transactions where team_name capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERR_CODE = "ATTACK_TRANSACTION_EXCEPTION_ROLLED_BACK"
  MSG = "AttackTransaction raised an rollback_exception. Transaction rolled back."

class FailedSettingActorAsEnemyCaptorRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERR_CODE = "FAILED_CAPTOR_PROPERTY_UPDATE_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Updating a combatant's victor consistency during an attack transaction failed. The transaction was rolled back "
    "before raising this exception."
  )

class FailedEnemyRemovalFromSquareRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERR_CODE = "FAILED_PRISONER_REMOVAL_FROM_SQUARE_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Removing a captured enemy from its square_name failed during an attack transaction. The transaction was "
    "rolled back before raising this exception."
  )

class FailedHostageAdditionRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERR_CODE = "FAILED_HOSTAGE_ADDITION_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Adding a prisoner failed during an attack transaction. The transaction was rolled back before raising this "
    "exception."
  )

class FailedRemovalFromRosterRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERR_CODE = "FAILED_CAPTIVE_REMOVAL_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Removing a captured owner from the team_name roster failed during an attack transaction. The transaction was rolled "
    "back before raising this exception."
  )

class FailedCapturedPiecFromBoardRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERR_CODE = "FAILED_CAPTURED_PIEC_FROM_BOARD_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Removing a captured owner from the board failed during an attack notification. The notification was rolled back "
    "before this rollback_exception was raised."
  )


class FailedRemovalFromBoardRolledBackException(RolledBackAttackTransactionException):
  """"""
  ERR_CODE = "FAILED_PIECE_REMOVAL_FROM_BOARD_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Removing a captured owner from the board failed during an attack transaction. The transaction was rolled "
    "back before raising this exception."
  )
