# src/chess/persona/validator/exception/ransom.py

"""
Module: chess.persona.validator.exception.ransom
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BoundsException
from chess.persona import PersonaException

__all__ = [
    # ======================# PERSONA_RANSOM_BOUNDS EXCEPTION #======================#
    "PersonaRansomBoundsException",
]


# ======================# PERSONA_RANSOM_BOUNDS EXCEPTION #======================#
class PersonaRansomBoundsException(PersonaException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Persona lookup failed because the ransom value was not permitted for the Persona
        attribute.

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
    ERROR_CODE = "PERSONA_RANSOM_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "PersonaLookup failed: Target was outside the set of possible Persona ransoms."