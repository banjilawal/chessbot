# src/chess/system/transaction/failure.py

"""
Module: chess.system.transaction
Author: Banji Lawal
Created: 2025-10-015
version: 1.0.0
"""

from chess.system import OperationFailedException, RollbackException


__all__ = [
    # ======================# TRANSACTION_FAILURE #======================#
    "TransactionFailedException",
]


# ======================# TRANSACTION_FAILURE #======================#
class TransactionFailedException(OperationFailedException, RollbackException):
    """
    # ROLE: Exception Wrapper, Integrity Debugging, State Restoration,

    # RESPONSIBILITIES:
    1.  Wraps a transaction DebugException and indicates that the transaction was rolled back before the
        the exception chain was sent.

    # PARENT:
        *   RollbackException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TRANSACTION_FAILURE"
    DEFAULT_MESSAGE = "Transaction failed. The transaction was rolled back before the exception chain was raised."