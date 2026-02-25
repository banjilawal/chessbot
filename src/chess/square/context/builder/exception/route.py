# src/chess/square/context/builder/exception/route.py

"""
Module: chess.square.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SQUARE_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
    "SquareContextBuildRouteException",
]

from chess.square import SquareContextException
from chess.system import  NoExecutionRouteException


# ======================# NO_SQUARE_CONTEXT_BUILD_ROUTE EXCEPTION #======================#
class SquareContextBuildRouteException(SquareContextException,  NoExecutionRouteException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
   1.  A failing BuildResult was returned because there was no build route was provided for the
        SquareContext attribute.

    # PARENT:
        *   SquareContextDebugException
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    Non
    """
    ERR_CODE = "NO_SQUARE_CONTEXT_BUILD_ROUTE_ERROR"
    MSG = "SquareContext build failed: No build route existed for the attribute."