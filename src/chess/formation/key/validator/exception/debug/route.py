# src/chess/formation/key/validator/exception/debug/route.py

"""
Module: chess.formation.key.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_FORMATION_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "FormationKeyValidationRouteException",
]

from chess.formation import FormationKeyException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_FORMATION_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class FormationKeyValidationRouteException(FormationKeyException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the FormationKey validation failed because there was no build route for the FormationKey key.

    # PARENT:
        *   FormationKeyException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_FORMATION_KEY_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "FormationKey validation failed: No validation route was provided for the Formation attribute."