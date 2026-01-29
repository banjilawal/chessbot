# src/chess/system/collectionoperation/insertion/exception/route.py

"""
Module: chess.system.collection.operation.insertion.exception.route
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

__all__ = [
    # ======================# NO_INSERTION_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
    "NoInsertionRouteException",
]

from chess.system import NoExecutionRouteException


# ======================# NO_INSERTION_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
class NoInsertionRouteException(NoExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a insertion failed because there was no execution logic for one the different 
        insertion behaviors.

    # PARENT:
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_INSERTION_ROUTE_FOR_SELECTED_OPTION_ERROR"
    DEFAULT_MESSAGE = "Insertion failed: No insertion route was defined for the specified option."