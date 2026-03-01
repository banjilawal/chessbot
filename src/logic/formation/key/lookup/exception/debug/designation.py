# src/logic/formation/key/lookup/exception/debug/designation.py

"""
Module: logic.formation.key.lookup.exception.debug.designation
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from logic.system import BoundsException
from logic.formation import FormationException

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
    ERR_CODE = "FORMATION_DESIGNATION_BOUNDS_EXCEPTION"
    MSG = "FormationLookup failed: Target was outside the set of possible Formation designations."
