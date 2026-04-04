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
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a Formation lookup failed because the designation value was not permitted for the Formation
        attribute.

    Super Class:
        *   FormationException
        *   BoundsException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "FORMATION_DESIGNATION_BOUNDS_EXCEPTION"
    MSG = "FormationLookupProcess failed: Target was outside the set of possible Formation designations."
