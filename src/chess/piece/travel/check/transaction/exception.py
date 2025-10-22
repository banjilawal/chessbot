# src/chess/vector/travel_exception.py

"""
Module: chess.vector.exception
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
=======================TRANSACTION EXCEPTIONS ARE ALWAYS ROLL_BACK_EXCEPTION SUBCLASSES======================#
=============================================================================================================#
"""

# ======================# ROLLED BACK ATTACK TRANSACTION EXCEPTIONS #======================#
class AttackTransactionException(AttackEventException, RollbackException):
  """
  RollBackCapture exceptions should be raised in ACID transactions where team capture can
  raise an err. Do not use directly. Subclasses give details useful for debugging.
  """
  ERROR_CODE = "ATTACK_TRANSACTION_ERROR_ROLLED_BACK"
  DEFAULT_MESSAGE = "AttackTransaction raised an exception. Transaction rolled back."

class FailedCaptorPropertyUpdateRolledBackException(AttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_CAPTOR_PROPERTY_UPDATE_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Updating a prisoner's captor field during an attack notification failed.  The notification was rolled back "
    "before this exception was raised."
  )

class FailedPrisonerRemovalFromSquareRolledBackException(AttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_PRISONER_REMOVAL_FROM_SQUARE_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Removing a captured piece from the square it was occupying failed during a notification. The notification "
    "was rolled back before this exception was raised."
  )

class FailedHostageAdditionRolledBackException(AttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_HOSTAGE_ADDITION_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Adding a hostage failed during an attack notification. The notification was rolled back before this "
    "exception was raised."
  )

class FailedRemovalFromRosterRolledBackException(AttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_CAPTIVE_REMOVAL_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Removing a captured team member failed during an attack notification. The notification was rolled back "
    "before this exception was raised."
  )

class FailedCapturedPiecFromBoardRolledBackException(AttackTransactionException):
  """"""
  ERROR_CODE = "FAILED_CAPTURED_PIEC_FROM_BOARD_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Removing a captured piece from the board failed during an attack notification. The notification was rolled back "
    "before this exception was raised."
  )