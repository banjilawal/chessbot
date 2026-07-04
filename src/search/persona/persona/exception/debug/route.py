# src/logic/persona/key/lookup/exception/debug/route.py

"""
Module: logic.persona.key.lookup.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from model.state.catalog.persona import PersonaException
from system import ExecutionRouteException

__all__ = [
    # ======================# NO_PERSONA_LOOKUP_ROUTE EXCEPTION #======================#
    "PersonaLookupRouteException",
]


# ======================# NO_PERSONA_LOOKUP_ROUTE EXCEPTION #======================#
class PersonaLookupRouteException(PersonaException, ExecutionRouteException):
    """
    Role:Fallback Result

    Responsibilities:
    1. Indicate that PersonaLookupProcess did not handle a build option or parameter with its own execution route.

    Super Class:
        *   PersonaException
        *   ExecutionRouteException


    # PROVIDES
    None


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_PERSONA_LOOKUP_ROUTE_EXCEPTION"
    MSG = "PersonaLookupProcess failed: No search route was provided for a Persona attribute."