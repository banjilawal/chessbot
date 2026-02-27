# src/chess/vector/rollback_exception.py

"""
Module: chess.vector.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import RollbackException
from chess.piece import AttackEventException

__all__ = [
  'AttackTransactionException',
  'FailedCaptorPropertyUpdateRolledBackException',
  'FailedPrisonerRemovalFromSquareRolledBackException',
  'FailedHostageAdditionRolledBackException',
  'FailedRemovalFromRosterRolledBackException',
  'FailedCapturedPiecFromBoardRolledBackException',
]

"""
=============================================================================================================#
=======================TRANSACTION EXCEPTION ARE ALWAYS ROLL_BACK_EXCEPTION SUBCLASSES======================#
=============================================================================================================#
"""

#======================# ROLLED BACK ATTACK TRANSACTION EXCEPTION #======================#
class AttackTransactionException(AttackEventException, RollbackException):
  """
  RollBackCapture exception should be raised in ACID transactions where team_name capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERR_CODE = "ATTACK_TRANSACTION_EXCEPTION_ROLLED_BACK"
  MSG = "AttackTransaction raised an rollback_exception. Transaction rolled back."

class FailedCaptorPropertyUpdateRolledBackException(AttackTransactionException):
  """"""
  ERR_CODE = "FAILED_CAPTOR_PROPERTY_UPDATE_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Updating a combatant's victor consistency during an attack notification failed.  The notification was rolled back "
    "before this rollback_exception was raised."
  )

class FailedPrisonerRemovalFromSquareRolledBackException(AttackTransactionException):
  """"""
  ERR_CODE = "FAILED_PRISONER_REMOVAL_FROM_SQUARE_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Removing a captured owner from the square_name it was occupying failed during a notification. The notification "
    "was rolled back before this rollback_exception was raised."
  )

class FailedHostageAdditionRolledBackException(AttackTransactionException):
  """"""
  ERR_CODE = "FAILED_HOSTAGE_ADDITION_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Adding a prisoner failed during an attack notification. The notification was rolled back before this "
    "rollback_exception was raised."
  )

class FailedRemovalFromRosterRolledBackException(AttackTransactionException):
  """"""
  ERR_CODE = "FAILED_CAPTIVE_REMOVAL_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Removing a captured team_name member failed during an attack notification. The notification was rolled back "
    "before this rollback_exception was raised."
  )

class FailedCapturedPiecFromBoardRolledBackException(AttackTransactionException):
  """"""
  ERR_CODE = "FAILED_CAPTURED_PIEC_FROM_BOARD_ROLLED_BACK_EXCEPTION"
  MSG = (
    "Removing a captured owner from the board failed during an attack notification. The notification was rolled back "
    "before this rollback_exception was raised."
  )