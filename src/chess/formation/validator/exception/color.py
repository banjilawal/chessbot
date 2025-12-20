# src/chess/formation/number_bounds_validator/exception/color.py

"""
Module: chess.formation.number_bounds_validator.exception.color
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import InvalidBattleOrderException
from chess.system import BoundsException, GameColorException

__all__ = [
    # ======================# ORDER COLOR BOUNDS EXCEPTION #======================#
    "OrderColorBoundsException",
]


# ======================# ORDER COLOR BOUNDS EXCEPTION #======================#
class OrderColorBoundsException(InvalidBattleOrderException, BoundsException, GameColorException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a color is outside the range of acceptable BattleOrder colors.

    # PARENT:
        *   InvalidBattleOrderException
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

