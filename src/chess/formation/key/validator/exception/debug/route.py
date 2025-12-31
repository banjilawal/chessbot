# src/chess/formation/validator/exception/debug/route.py

"""
Module: chess.formation.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import UnhandledRouteException
from chess.formation import FormationSuperKeyException



__all__ = [
    # ======================# UNHANDLED_FORMATION_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "FormationSuperKeyValidationRouteException",
]


# ======================# UNHANDLED_FORMATION_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class FormationSuperKeyValidationRouteException(FormationSuperKeyException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate failed FormationSuperKey validation because no validation route for its attribute.

    # PARENT:
        *   UnhandledRouteException
        *   FormationSuperKeyException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_FORMATION_SUPER_KEY_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = (
        "FormationSuperKey validation failed: No validation route was provided for the Formation attribute."
    )