# src/chess/formation/key/lookup/exception/debug/route.py

"""
Module: chess.formation.key.lookup.exception.debug.route
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import FormationException
from chess.system import NoExecutionRouteException

__all__ = [
    # ======================# NO_FORMATION_LOOKUP_ROUTE EXCEPTION #======================#
    "FormationLookupRouteException",
]


# ======================# NO_FORMATION_LOOKUP_ROUTE EXCEPTION #======================#
class FormationLookupRouteException(FormationException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result

    # RESPONSIBILITIES:
    1. Indicate that FormationLookup did not handle a build option or parameter with its own execution route.

    # PARENT:
        *   FormationException
        *   NoExecutionRouteException


    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_FORMATION_LOOKUP_ROUTE_ERROR"
    DEFAULT_MESSAGE = "FormationLookup failed: No search route was provided for a Formation attribute."