# src/chess/formation/validator/exception/name.py

"""
Module: chess.formation.validator.exception.name
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import InvalidFormationException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# ORDER NAME BOUNDS EXCEPTION #======================#
    "OrderNameBoundsException",
]


# ======================# ORDER NAME BOUNDS EXCEPTION #======================#
class OrderNameBoundsException(InvalidFormationException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a designation is outside the range of acceptable Formation names.

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
    ERROR_CODE = "ORDER_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Name is not included in the set of permissible order names."