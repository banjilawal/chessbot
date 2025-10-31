# src/chess/system/transaction/exception.py

"""
Module: chess.system.transaction.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ChessException, RollbackException

__all__ = [
  'TransactionException',
  'RolledBackTransactionException',
]


class TransactionException(ChessException):
  """
  Super class of all exceptions `Transaction` object raises. Do not use directly. Subclasses give
  details useful for debugging. This class exists primarily to allow catching all `Transaction`
  exceptions.
  """
  ERROR_CODE = "TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "Transaction raised an rollback_exception."


class RolledBackTransactionException(TransactionException, RollbackException):
  """
  Super class of all exceptions `Transaction` object raises. Do not use directly. Subclasses give
  details useful for debugging. This class exists primarily to allow catching all `Transaction`
  exceptions.
  """
  ERROR_CODE = "TRANSACTION_ERROR"
  DEFAULT_MESSAGE = "Transaction raised an rollback_exception."


