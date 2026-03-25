# src/logic/persona/key/validation/exception/debug/route.py

"""
Module: logic.persona.key.validation.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PERSONA_KEY_VALIDATION_ROUTE EXCEPTION #======================#
    "PersonaKeyValidationRouteException",
]

from logic.persona import PersonaKeyException
from logic.system import ExecutionRouteException


# ======================# NO_PERSONA_KEY_VALIDATION_ROUTE EXCEPTION #======================#
class PersonaKeyValidationRouteException(PersonaKeyException, ExecutionRouteException):
    """
    Role:Fallback Result, Debugging

    Responsibilities:
    1.  Indicate that the PersonaKey validation failed because there was no build route for the PersonaKey key.

    Super Class:
        *   PersonaKeyException
        *   ExecutionRouteException

    # PROVIDES
    None


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_PERSONA_KEY_VALIDATION_ROUTE_EXCEPTION"
    MSG = "PersonaKey validation failed: No validation route was provided for the Persona attribute."