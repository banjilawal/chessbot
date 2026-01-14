# src/chess/persona/key/builder/exception/route.py

"""
Module: chess.persona.key.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# UNHANDLED_PERSONA_KEY_BUILD_ROUTE EXCEPTION #======================#
    "PersonaKeyBuildRouteException",
]

from chess.persona import PersonaKeyException
from chess.system import NoBuildRouteException


# ======================# UNHANDLED_PERSONA_KEY_BUILD_ROUTE EXCEPTION #======================#
class PersonaKeyBuildRouteException(PersonaKeyException, NoBuildRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PersonaKey build failed because there was no build route for the Persona key.

    # PARENT:
        *   PersonaKeyException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PERSONA_KEY_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "PersonaKey build failed: No build path existed for the Persona key."