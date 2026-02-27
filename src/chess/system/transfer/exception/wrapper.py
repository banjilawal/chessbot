# src/chess/system/transfer/exception/wrapper.py

"""
Module: chess.system.transfer.exception.wrapper
Author: Banji Lawal
Created: 2026-02-01
version: 1.0.0
"""

from chess.system import OperationException

__all__ = [
    # ======================# TRANSFER_FAILURE #======================#
    "TransferException",
]


# ======================# TRANSFER_FAILURE #======================#
class TransferException(OperationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an exception prevented a transfer operation from completing successfully.
    2.  Wrap an exception that hits the try-finally block of a Transfer method.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TRANSFER_FAILED_EXCEPTION"
    MSG = "transfer failed."