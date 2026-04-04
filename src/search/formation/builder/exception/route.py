# src/logic/formation/key/build/exception/route.py

"""
Module: logic.formation.key.build.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NO_FORMATION_KEY_BUILD_ROUTE EXCEPTION #======================#
    "FormationKeyBuildRouteException",
]

from catalog.formation import FormationKeyException
from logic.system import ExecutionRouteException


# ======================# NO_FORMATION_KEY_BUILD_ROUTE EXCEPTION #======================#
class FormationKeyBuildRouteException(FormationKeyException, ExecutionRouteException):
    """
    Role:Fallback Result, Debugging

    Responsibilities:
    1.  Indicate that the FormationKey build failed because there was no build route for the Formation key.

    Super Class:
        *   FormationKeyException
        *   ExecutionRouteException

    # PROVIDES
    None


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_FORMATION_KEY_BUILD_ROUTE_EXCEPTION"
    MSG = "FormationKey build failed: No build path existed for the Formation key."