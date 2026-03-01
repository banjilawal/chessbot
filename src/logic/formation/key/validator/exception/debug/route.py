# src/logic/formation/key/validator/exception/debug/route.py

"""
Module: logic.formation.key.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_FORMATION_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "FormationKeyValidationRouteException",
]

from logic.formation import FormationKeyException
from logic.system import ExecutionRouteException


# ======================# NO_FORMATION_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class FormationKeyValidationRouteException(FormationKeyException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the FormationKey validation failed because there was no build route for the FormationKey key.

    # PARENT:
        *   FormationKeyException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_FORMATION_KEY_VALIDATION_ROUTE_EXCEPTION"
    MSG = "FormationKey validation failed: No validation route was provided for the Formation attribute."