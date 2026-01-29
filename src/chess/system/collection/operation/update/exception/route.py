# src/chess/system/collectionoperation/update/exception/route.py

"""
Module: chess.system.collection.operation.update.exception.route
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

__all__ = [
    # ======================# NO_UPDATE_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
    "NoUpdateRouteException",
]

from chess.system import NoExecutionRouteException


# ======================# NO_UPDATE_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
class NoUpdateRouteException(NoExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a update failed because there was no execution logic for one the different 
        update behaviors.

    # PARENT:
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_UPDATE_ROUTE_FOR_SELECTED_OPTION_ERROR"
    DEFAULT_MESSAGE = "Update failed: No update route was defined for the specified option."