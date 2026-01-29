# src/chess/system/data/operation/deletion/exception/route.py

"""
Module: chess.system.data.operation.deletion.exception.route
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

__all__ = [
    # ======================# NO_DELETION_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
    "NoDeletionRouteException",
]

from chess.system import NoExecutionRouteException


# ======================# NO_DELETION_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
class NoDeletionRouteException(NoExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a deletion failed because there was no execution logic for one the different
        deletion behaviors.

    # PARENT:
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_DELETION_ROUTE_FOR_SELECTED_OPTION_ERROR"
    DEFAULT_MESSAGE = "Deletion failed: No deletion route was defined for the specified option."