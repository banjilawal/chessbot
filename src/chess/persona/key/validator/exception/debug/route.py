# src/chess/persona/key/validator/exception/debug/route.py

"""
Module: chess.persona.key.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.persona import PersonaSuperKey
from chess.system import UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_PERSONA_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "PersonaSuperKeyValidationRouteException",
]


# ======================# UNHANDLED_PERSONA_SUPER_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class PersonaSuperKeyValidationRouteException(PersonaSuperKey, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate failed PersonaSuperKey validation because no validation route for its attribute.

    # PARENT:
        *   PersonaSuperKey
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PERSONA_SUPER_KEY_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "PersonaSuperKey validation failed: No validation route was provided for the Persona attribute."