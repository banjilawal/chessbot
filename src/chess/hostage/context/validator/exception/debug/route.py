# src/chess/hostage/context/validator/exception/debug/route.py

"""
Module: chess.hostage.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_CAPTIVITY_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "CaptivityContextValidationRouteException",
]

from chess.hostage import CaptivityContextException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_CAPTIVITY_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class CaptivityContextValidationRouteException(CaptivityContextException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the CaptivityContext validation failed because there was no validation route for the
        CaptivityContext key.

    # PARENT:
        *   CaptivityContextException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_CAPTIVITY_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "CaptivityContext validation failed: No validation route was provided for a CaptivityContext attribute."
    )