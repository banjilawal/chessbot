# src/logic/square/context/validator/exception/debug/route.py

"""
Module: logic.square.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_SQUARE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "SquareContextValidationRouteException",
]

from logic.square.context import SquareContextDebugException
from logic.system import  ExecutionRouteException


# ======================# NO_SQUARE_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class SquareContextValidationRouteException(SquareContextDebugException, ExecutionRouteException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because there was no validation route for the  candidate
        square_context's attribute.

    # PARENT:
        *   SquareContextDebugException
        *   ExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    Non
    """
    ERR_CODE = "NO_SQUARE_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    MSG = (
        "SquareContext validation failed: No validation route existed for the candidate's attribute."
    )