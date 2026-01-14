# src/chess/system/transaction/exception/rollback.py

"""
Module: chess.system.transaction.exception.rollback
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
  # ====================== ROLLBACK_OPERATION EXCEPTION #======================#
  'RollbackException',
]


#====================== ROLLBACK_OPERATION EXCEPTION #======================#
class RollbackException(ChessException):
  """
  # ROLE: Error Rollback, Integrity Debugging, State Restoration,

  # RESPONSIBILITIES:
  1.  Indicate that an operation that failed was is rolled back before the exception chain was sent.

  # PARENT:
      *   ChessException

  # PROVIDES:
  None

  # LOCAL ATTRIBUTES:
  None

  # INHERITED ATTRIBUTES:
  None
  """
  ERROR_CODE = "ROLLBACK_OPERATION"
  DEFAULT_MESSAGE = "Operation failed and rolled back."

