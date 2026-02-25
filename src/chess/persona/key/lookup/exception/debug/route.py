# src/chess/persona/key/lookup/exception/debug/route.py

"""
Module: chess.persona.key.lookup.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.persona import PersonaException
from chess.system import NoExecutionRouteException

__all__ = [
    # ======================# NO_PERSONA_LOOKUP_ROUTE EXCEPTION #======================#
    "PersonaLookupRouteException",
]


# ======================# NO_PERSONA_LOOKUP_ROUTE EXCEPTION #======================#
class PersonaLookupRouteException(PersonaException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result

    # RESPONSIBILITIES:
    1. Indicate that PersonaLookup did not handle a build option or parameter with its own execution route.

    # PARENT:
        *   PersonaException
        *   NoExecutionRouteException


    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_PERSONA_LOOKUP_ROUTE_ERROR"
    MSG = "PersonaLookup failed: No search route was provided for a Persona attribute."