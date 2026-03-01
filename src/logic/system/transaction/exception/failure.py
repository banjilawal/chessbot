# src/logic/system/transaction/failure.py

"""
Module: logic.system.transaction
Author: Banji Lawal
Created: 2025-10-015
version: 1.0.0
"""

from logic.system import OperationException, RollbackException


__all__ = [
    # ======================# TRANSACTION_FAILURE #======================#
    "TransactionException",
]


# ======================# TRANSACTION_FAILURE #======================#
class TransactionException(OperationException, RollbackException):
    """
    # ROLE: Exception Wrapper, Integrity Debugging, State Restoration,

    # RESPONSIBILITIES:
    1.  Wraps a transaction DebugException and indicates that the transaction was rolled back before the
        the exception chain was sent.

    # PARENT:
        *   RollbackException
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TRANSACTION_FAILURE"
    MSG = "Transaction failed. The transaction was rolled back before the exception chain was raised."