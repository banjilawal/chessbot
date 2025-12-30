# src/chess/formation/key/lookup/exception/debug/color.py

"""
Module: chess.formation.key.lookup.exception.debug.color
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BoundsException
from chess.formation import FormationException

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
    ERROR_CODE = "FORMATION_COLOR_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "FormationLookup failed: Target was outside the set of possible Formation colors."