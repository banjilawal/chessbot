# src/chess/system/transfer/exception/route.py

"""
Module: chess.system.transfer.exception.route
Author: Banji Lawal
Created: 2026-02-01
version: 1.0.0
"""

__all__ = [
    # ======================# NO_TRANSFER_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
    "TransferRouteException",
]

from chess.system import ExecutionRouteException


# ======================# NO_TRANSFER_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
class TransferRouteException(ExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Super Exception

    # RESPONSIBILITIES:
    1.  Indicate that a transfer failed because there was no execution logic for one the different 
        transfer behaviors.

    # PARENT:
        *   ExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_TRANSFER_ROUTE_FOR_SELECTED_OPTION_EXCEPTION"
    MSG = "Transfer failed: No transfer route was defined for the specified option."