# src/chess/formation/validator/exception/square_name.py

"""
Module: chess.formation.validator.exception.square_name
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import InvalidFormationException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# ORDER SQUARE BOUNDS EXCEPTION #======================#
    "OrderSquareBoundsException",
]


# ======================# ORDER SQUARE BOUNDS EXCEPTION #======================#
class OrderSquareBoundsException(InvalidFormationException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a square_name is outside the range of acceptable Formation squares.

    # PARENT:
        *   InvalidFormationException
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

