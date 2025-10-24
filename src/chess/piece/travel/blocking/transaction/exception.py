# src/chess/piece/travel/blocking/transaction/rollback_exception.py

"""
Module: chess.piece.travel.blocking.transaction.rollback_exception
Author: Banji Lawal
Created: 2025-10-21
version: 1.0.0
"""

from chess.system import RollbackException
from chess.piece import TravelTransactionException

"""
=============================================================================================================#
==============LOG_ENCOUNTER_TRANSACTION EXCEPTIONS ARE ALWAYS ROLL_BACK_EXCEPTION SUBCLASSES=================#
=============================================================================================================#
"""

__all__ = [
  'BlockedPathTransactionException',
  'FailedDiscoveryAdditionRolledBackException',
]

class BlockedPathTransactionException(TravelTransactionException):
  """"""
  ERROR_CODE = "BLOCKED_PATH_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = (
    "BlockedPathTransaction failed. The transaction was rolled back before raising this rollback_exception."
  )

class FailedDiscoveryAdditionRolledBackException(BlockedPathTransactionException, RollbackException):
  """"""
  ERROR_CODE = "FAILED_DISCOVERY_ADDITION_ROLLED_BACK_ERROR"
  DEFAULT_MESSAGE = (
    "Adding a new Discovery failed during a BlockedPathTransaction. The transaction was rolled back before "
    "raising this rollback_exception."
  )




