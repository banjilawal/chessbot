# src/chess/persona/key/validator/exception/debug/route.py

"""
Module: chess.persona.key.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PERSONA_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "PersonaKeyValidationRouteException",
]

from chess.persona import PersonaKeyException
from chess.system import NoValidationRouteException


# ======================# UNHANDLED_PERSONA_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class PersonaKeyValidationRouteException(PersonaKeyException, NoValidationRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PersonaKey validation failed because there was no build route for the PersonaKey key.

    # PARENT:
        *   PersonaKeyException
        *   NoValidationRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PERSONA_KEY_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "PersonaKey validation failed: No validation route was provided for the Persona attribute."