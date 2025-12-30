# src/chess/persona/key/lookup/exception/debug/route.py

"""
Module: chess.persona.key.lookup.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.persona import PersonaException
from chess.system import UnhandledRouteException

__all__ = [
    # ======================# UNHANDLED_PERSONA_LOOKUP_ROUTE EXCEPTION #======================#
    "PersonaLookupRouteException",
]


# ======================# UNHANDLED_PERSONA_LOOKUP_ROUTE EXCEPTION #======================#
class PersonaLookupRouteException(PersonaException, UnhandledRouteException):
    """
    # ROLE: Fallback Result

    # RESPONSIBILITIES:
    1. Indicate that PersonaLookuper did not handle a build option or parameter with its own execution route.

    # PARENT:
        *   PersonaException
        *   UnhandledRouteException


    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_PERSONA_LOOKUP_ROUTE_ERROR"
    DEFAULT_MESSAGE = "PersonaLookup failed: No search route was provided for a Persona attribute."