# src/chess/square/context/validator/exception/debug/route.py

"""
Module: chess.square.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SQUARE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "SquareContextValidationRouteException",
]

from chess.square import SquareContextDebugException
from chess.system import  NoExecutionRouteException


# ======================# NO_SQUARE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class SquareContextValidationRouteException(SquareContextDebugException,  NoExecutionRouteException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because there was no validation route for the  candidate
        square_context's attribute.

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
    ERROR_CODE = "NO_SQUARE_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "SquareContext validation failed: No validation route existed for the candidate's attribute."
    )