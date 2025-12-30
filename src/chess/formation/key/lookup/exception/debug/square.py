# src/chess/formation/key/lookup/exception/debug/square.py

"""
Module: chess.formation.key.lookup.exception.debug.square
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.formation import FormationException
from chess.system import BoundsException

__all__ = [
    # ======================# FORMATION_SQUARE_NAME_BOUNDS EXCEPTION #======================#
    "FormationSquareBoundsException",
]


# ======================# FORMATION_SQUARE_NAME_BOUNDS EXCEPTION #======================#
class FormationSquareBoundsException(FormationException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Formation lookup failed because the square value was not permitted for the Formation
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
    ERROR_CODE = "FORMATION_SQUARE_NAME_BOUNDS"
    DEFAULT_MESSAGE = "FormationLookup failed: Target was outside the set of possible Formation square names."