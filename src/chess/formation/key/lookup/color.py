# src/chess/formation/validator/exception/color.py

"""
Module: chess.formation.validator.exception.color
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import InvalidFormationException
from chess.system import BoundsException, GameColorException

__all__ = [
    # ======================# FORMATION_LOOKUP_BY_COLOR EXCEPTION #======================#
    "FormationLookupByColorException",
]


# ======================# FORMATION_LOOKUP_BY_COLOR EXCEPTION #======================#
class FormationLookupByColorException(InvalidFormationException, BoundsException, GameColorException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a color is outside the range of acceptable Formation colors.

    # PARENT:
        *   InvalidFormationException
        *   BoundsException
        *   GameColorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "FORMATION_LOOKUP_BY_COLOR_ERROR"
    DEFAULT_MESSAGE = "Color is not included in the set of permissible order colors."

