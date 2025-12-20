# src/chess/formation/validator/exception/square.py

"""
Module: chess.formation.validator.exception.square
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import InvalidBattleOrderException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# ORDER SQUARE BOUNDS EXCEPTION #======================#
    "OrderSquareBoundsException",
]


# ======================# ORDER SQUARE BOUNDS EXCEPTION #======================#
class OrderSquareBoundsException(InvalidBattleOrderException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a square is outside the range of acceptable BattleOrder squares.

    # PARENT:
        *   InvalidBattleOrderException
        *   BoundsException
        *   NameException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ORDER_SQUARE_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Square is not included in the set of permissible order squares."

