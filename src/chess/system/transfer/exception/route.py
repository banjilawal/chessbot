# src/chess/system/transfer/exception/route.py

"""
Module: chess.system.transfer.exception.route
Author: Banji Lawal
Created: 2026-02-01
version: 1.0.0
"""

__all__ = [
    # ======================# NO_TRANSFER_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
    "NoTransferRouteException",
]

from chess.system import NoExecutionRouteException


# ======================# NO_TRANSFER_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
class NoTransferRouteException(NoExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a transfer failed because there was no execution logic for one the different 
        transfer behaviors.

    # PARENT:
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_TRANSFER_ROUTE_FOR_SELECTED_OPTION_ERROR"
    DEFAULT_MESSAGE = "Transfer failed: No transfer route was defined for the specified option."