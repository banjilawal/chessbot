# src/chess/system/collection/operation/collision/exception/route.py

"""
Module: chess.system.collection.operation.collision.exception.route
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

__all__ = [
    # ======================# NO_COLLISION_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
    "NoCollisionRouteException",
]

from chess.system import NoExecutionRouteException


# ======================# NO_COLLISION_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
class NoCollisionRouteException(NoExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a collision failed because there was no execution logic for one the different 
        collision behaviors.

    # PARENT:
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_COLLISION_ROUTE_FOR_SELECTED_OPTION_ERROR"
    DEFAULT_MESSAGE = "Collision failed: No collision route was defined for the specified option."