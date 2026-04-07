# src/logic/formation/key/lookup/exception/debug/persona.py

"""
Module: logic.formation.key.lookup.exception.debug.persona
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from system import BoundsException
from model.catalog.formation import FormationException

__all__ = [
    # ======================# FORMATION_PERSONA_BOUNDS EXCEPTION #======================#
    "FormationPersonaBoundsException",
]


# ======================# FORMATION_PERSONA_BOUNDS EXCEPTION #======================#
class FormationPersonaBoundsException(FormationException, BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a Formation lookup failed because the persona value was not permitted for the Formation
        attribute.

    Super Class:
        *   FormationException
        *   BoundsException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "FORMATION_PERSONA_BOUNDS_EXCEPTION"
    MSG = "FormationLookupProcess failed: Target was outside the set of possible Formation personas."
