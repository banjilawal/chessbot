# src/logic/persona/validation/exception/ransom.py

"""
Module: logic.persona.validation.exception.ransom
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from system import BoundsException
from catalog.persona import PersonaException

__all__ = [
    # ======================# PERSONA_RANSOM_BOUNDS EXCEPTION #======================#
    "PersonaRansomBoundsException",
]


# ======================# PERSONA_RANSOM_BOUNDS EXCEPTION #======================#
class PersonaRansomBoundsException(PersonaException, BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a Persona lookup failed because the ransom value was not permitted for the Persona
        attribute.

    Super Class:
        *   PersonaException
        *   BoundsException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PERSONA_RANSOM_BOUNDS_EXCEPTION"
    MSG = "PersonaLookupProcess failed: Target was outside the set of possible Persona ransoms."