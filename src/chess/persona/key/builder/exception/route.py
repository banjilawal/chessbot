# src/chess/persona/builder/exception/route.py

"""
Module: chess.persona.builder.exception.route
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.persona import PersonaSuperKeyException
from chess.system import UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_PERSONA_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
    "PersonaSuperKeyBuildRouteException",
]


# ======================# UNHANDLED_PERSONA_SUPER_KEY_BUILD_ROUTE EXCEPTION #======================#
class PersonaSuperKeyBuildRouteException(PersonaSuperKeyException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the PersonaSuperKey build failed because there was no build route for the Persona attribute.

    # PARENT:
        *   PersonaSuperKeyException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PERSONA_SUPER_KEY_BUILD_ROUTE_ERROR"
    DEFAULT_MESSAGE = "PersonaSuperKey build failed: No build path existed for the Persona attribute."