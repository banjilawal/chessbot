# src/logic/formation/key/lookup/exception/debug/route.py

"""
Module: logic.formation.key.lookup.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from logic.formation import FormationException
from logic.system import ExecutionRouteException

__all__ = [
    # ======================# NO_FORMATION_LOOKUP_ROUTE EXCEPTION #======================#
    "FormationLookupRouteException",
]


# ======================# NO_FORMATION_LOOKUP_ROUTE EXCEPTION #======================#
class FormationLookupRouteException(FormationException, ExecutionRouteException):
    """
    Role:Fallback Result

    Responsibilities:
    1. Indicate that FormationLookup did not handle a build option or parameter with its own execution route.

    Super Class:
        *   FormationException
        *   ExecutionRouteException


    # PROVIDES
    None


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_FORMATION_LOOKUP_ROUTE_EXCEPTION"
    MSG = "FormationLookup failed: No search route was provided for a Formation attribute."