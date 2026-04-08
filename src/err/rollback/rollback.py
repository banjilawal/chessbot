# src/logic/system/transaction/exception/rollback.py

"""
Module: logic.system.transaction.exception.rollback
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from system import ChessException

__all__ = [
  # ====================== ERR.ROLLBACK_OPERATION EXCEPTION #======================#
  'RollbackException',
]


#====================== ERR.ROLLBACK_OPERATION EXCEPTION #======================#
class RollbackException(ChessException):
  """
  Role:Error Rollback, Integrity Debugging, State Restoration,

  Responsibilities:
  1.  Indicate that an operation that failed was is rolled back before the exception chain was sent.

  Super Class:
      *   ChessException

  # PROVIDES:
  None

  # LOCAL ATTRIBUTES:
  None

  # INHERITED ATTRIBUTES:
  None
  """
  ERR_CODE = "ROLLBACK_OPERATION"
  MSG = "Operation failed and rolled back."

