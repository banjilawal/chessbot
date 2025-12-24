# src/chess/formation/validator/exception/square.py

"""
Module: chess.formation.validator.exception.square
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.formation import InvalidFormationException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# FORMATION_SQUARE_BOUNDS EXCEPTION #======================#
    "FormationSquareBoundsException",
]


# ======================# FORMATION_SQUARE_BOUNDS EXCEPTION #======================#
class FormationSquareBoundsException(InvalidFormationException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that no opening formation is made from the square.

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

