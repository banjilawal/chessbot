# src/logic/hostage/context/validator/exception/debug/route.py

"""
Module: logic.hostage.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_CAPTIVITY_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "CaptivityContextValidationRouteException",
]

from logic.hostage import CaptivityContextException
from logic.system import ExecutionRouteException


# ======================# NO_CAPTIVITY_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class CaptivityContextValidationRouteException(CaptivityContextException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the CaptivityContext validation failed because there was no validation route for the
        CaptivityContext key.

    # PARENT:
        *   CaptivityContextException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_CAPTIVITY_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    MSG = (
        "CaptivityContext validation failed: No validation route was provided for a CaptivityContext attribute."
    )