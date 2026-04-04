# src/logic/persona/key/lookup/exception/debug/schema.py

"""
Module: logic.persona.key.lookup.exception.debug.schema
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from catalog.persona import PersonaException
from logic.system import BoundsException

__all__ = [
    # ======================# PERSONA_NAME_BOUNDS EXCEPTION #======================#
    "PersonaNameBoundsException",
]


# ======================# PERSONA_NAME_BOUNDS EXCEPTION #======================#
class PersonaNameBoundsException(PersonaException, BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a Persona lookup failed because the schema was not a key to any Persona variant.

    Super Class:
        *   PersonaException
        *   BoundsException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PERSONA_NAME_BOUNDS_EXCEPTION"
    MSG = "PersonaLookupProcess failed: No Persona entries use the target as their key."