# src/chess/node/context/validator/exception/debug/route.py

"""
Module: chess.node.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_NODE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "NodeContextValidationRouteException",
]

from chess.node import NodeContextException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_NODE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class NodeContextValidationRouteException(NodeContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the NodeContext validation failed because there was no validation route for the
        NodeContext key.

    # PARENT:
        *   NodeContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_NODE_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "NodeContext validation failed: No validation route was provided for a NodeContext attribute."