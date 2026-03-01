# src/logic/node/context/validator/exception/debug/route.py

"""
Module: logic.node.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_NODE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "NodeContextValidationRouteException",
]

from logic.node import NodeContextException
from logic.system import ExecutionRouteException


# ======================# NO_NODE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class NodeContextValidationRouteException(NodeContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the NodeContext validation failed because there was no validation route for the
        NodeContext key.

    # PARENT:
        *   NodeContextException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_NODE_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    MSG = "NodeContext validation failed: No validation route was provided for a NodeContext attribute."