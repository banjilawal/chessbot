# src/logic/formation/key/lookup/exception/debug/color.py

"""
Module: logic.formation.key.lookup.exception.debug.color
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from logic.system import BoundsException
from logic.formation import FormationException

__all__ = [
    # ======================# FORMATION_COLOR_BOUNDS EXCEPTION #======================#
    "FormationColorBoundsException",
]


# ======================# FORMATION_COLOR_BOUNDS EXCEPTION #======================#
class FormationColorBoundsException(FormationException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Formation lookup failed because the color value was not permitted for the Formation
        attribute.

    # PARENT:
        *   FormationException
        *   BoundsException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "FORMATION_COLOR_BOUNDS_EXCEPTION"
    MSG = "FormationLookup failed: Target was outside the set of possible Formation colors."