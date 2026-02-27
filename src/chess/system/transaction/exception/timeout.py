# src/chess/system/transaction/exception/timeout.py

"""
Module: chess.system.transaction.exception.timeout
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


__all__ = [
    # ====================== TRANSACTION_TIMEOUT EXCEPTION #======================#
    'TransactionTimeoutException',
]

from chess.system import ResourceUnavailableException, TransactionException


# ====================== TRANSACTION_TIMEOUT EXCEPTION #======================#
class TransactionTimeoutException(TransactionException, ResourceUnavailableException):
    """
    # ROLE: Error Tracing, Debugging, Super Exception

    # RESPONSIBILITIES:
    1.  Indicate that a transaction was not completed because it timed out waiting for a resource.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TRANSACTION_TIMEOUT_EXCEPTION"
    MSG = "The transaction was cancelled. It timed out waiting for a resource."