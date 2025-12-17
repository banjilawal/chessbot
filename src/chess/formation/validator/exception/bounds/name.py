# src/chess/formation/validator/exception/bounds/designation.py

"""
Module: chess.formation.validator.exception.bounds.designation
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import InvalidBattleOrderException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# ORDER NAME BOUNDS EXCEPTIONS #======================#
    "OrderNameBoundsException",
]


# ======================# ORDER NAME BOUNDS EXCEPTIONS #======================#
class OrderNameBoundsException(InvalidBattleOrderException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a designation is outside the range of acceptable BattleOrder names.

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
    ERROR_CODE = "ORDER_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Name is not included in the set of permissible order names."