# src/chess/formation/key/lookup/exception/debug/designation.py

"""
Module: chess.formation.key.lookup.exception.debug.designation
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BoundsException
from chess.formation import FormationException

__all__ = [
    # ======================# FORMATION_DESIGNATION_BOUNDS EXCEPTION #======================#
    "FormationDesignationBoundsException",
]


# ======================# FORMATION_DESIGNATION_BOUNDS EXCEPTION #======================#
class FormationDesignationBoundsException(FormationException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Formation lookup failed because the designation value was not permitted for the Formation
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
    ERROR_CODE = "FORMATION_DESIGNATION_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "FormationLookup failed: Target was outside the set of possible Formation designations."
