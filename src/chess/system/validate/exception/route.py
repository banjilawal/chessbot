# src/chess/system/validate/exception/route.py

"""
Module: chess.system.validate.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_VALIDATION_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
    "NoValidationRouteException",
]

from chess.system import NoExecutionRouteException


# ======================# NO_VALIDATION_ROUTE_FOR_SELECTED_OPTION EXCEPTION #======================#
class NoValidationRouteException(NoExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that a validation failed because there was no coverage for the selected validation option.

    # PARENT:
        *   NoExecutionRouteException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_VALIDATION_ROUTE_FOR_SELECTED_OPTION_ERROR"
    DEFAULT_MESSAGE = "Validation failed: No validation route was defined for the selected option."