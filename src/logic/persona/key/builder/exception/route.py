# src/logic/persona/key/builder/exception/route.py

"""
Module: logic.persona.key.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_PERSONA_KEY_BUILD_ROUTE EXCEPTION #======================#
    "PersonaKeyBuildRouteException",
]

from logic.persona import PersonaKeyException
from logic.system import ExecutionRouteException


# ======================# NO_PERSONA_KEY_BUILD_ROUTE EXCEPTION #======================#
class PersonaKeyBuildRouteException(PersonaKeyException, ExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PersonaKey build failed because there was no build route for the Persona key.

    # PARENT:
        *   PersonaKeyException
        *   ExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_PERSONA_KEY_BUILD_ROUTE_EXCEPTION"
    MSG = "PersonaKey build failed: No build path existed for the Persona key."