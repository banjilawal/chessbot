# src/chess/system/transaction/exception/rollback.py

"""
Module: chess.system.transaction.exception.rollback
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import TransactionException

__all__ = [
  #====================== ROLLED_BACK_TRANSACTION EXCEPTION #======================#
  'RollbackException',
]


#====================== ROLLBACK EXCEPTION #======================#
class RollbackException(TransactionException):
  """
    # ROLE: Error Tracing, Debugging

  # RESPONSIBILITIES:
  1.  Parent of exception raised when a Transaction is rolled back to its last checkpoint.

  # PARENT:
      *   TransactionException
      *   RollbackException

  # PROVIDES:
  RollbackException

  # LOCAL ATTRIBUTES:
  None

  # INHERITED ATTRIBUTES:
  None
  """
  ERROR_CODE = "ROLLED_BACK_TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "Transaction failed. The transaction was rolled back before raiing this exception."

