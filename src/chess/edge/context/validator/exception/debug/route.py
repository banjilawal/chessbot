# src/chess/edge/context/validator/exception/debug/route.py

"""
Module: chess.edge.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_EDGE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "EdgeContextValidationRouteException",
]

from chess.edge import EdgeContextException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_EDGE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class EdgeContextValidationRouteException(EdgeContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the EdgeContext validation failed because there was no validation route for the
        EdgeContext key.

    # PARENT:
        *   EdgeContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_EDGE_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "EdgeContext validation failed: No validation route was provided for a EdgeContext attribute."