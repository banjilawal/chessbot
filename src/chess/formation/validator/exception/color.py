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
    # ======================# ORDER COLOR BOUNDS EXCEPTION #======================#
    "FormationColorBoundsException",
]


# ======================# ORDER COLOR BOUNDS EXCEPTION #======================#
class FormationColorBoundsException(InvalidFormationException, BoundsException, GameColorException):
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
    ERROR_CODE = "ORDER_COLOR_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Color is not included in the set of permissible order colors."

