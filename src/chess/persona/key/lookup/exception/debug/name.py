# src/chess/persona/key/lookup/exception/debug/name.py

"""
Module: chess.persona.key.lookup.exception.debug.name
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.persona import PersonaException
from chess.system import BoundsException

__all__ = [
    # ======================# PERSONA_NAME_BOUNDS EXCEPTION #======================#
    "PersonaNameBoundsException",
]


# ======================# PERSONA_NAME_BOUNDS EXCEPTION #======================#
class PersonaNameBoundsException(PersonaException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Persona lookup failed because the name was not a key to any Persona variant.

    # PARENT:
        *   PersonaException
        *   BoundsException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "PersonaLookup failed: No Persona entries use the target as their key."