# src/chess/formation/key/builder/exception/route.py

"""
Module: chess.formation.key.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_FORMATION_KEY_BUILD_ROUTE EXCEPTION #======================#
    "FormationKeyBuildRouteException",
]

from chess.formation import FormationKeyException
from chess.system import NoExecutionRouteException


# ======================# NO_FORMATION_KEY_BUILD_ROUTE EXCEPTION #======================#
class FormationKeyBuildRouteException(FormationKeyException, NoExecutionRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the FormationKey build failed because there was no build route for the Formation key.

    # PARENT:
        *   FormationKeyException
        *   NoExecutionRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_FORMATION_KEY_BUILD_ROUTE_EXCEPTION"
    MSG = "FormationKey build failed: No build path existed for the Formation key."