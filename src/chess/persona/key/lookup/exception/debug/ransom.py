# src/chess/persona/validator/exception/ransom.py

"""
Module: chess.persona.validator.exception.ransom
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BoundsException
from chess.persona import InvalidPersonaException

__all__ = [
    # ======================# PERSONA RANSOM BOUNDS EXCEPTION #======================#
    "PersonaRansomBoundsException",
]


# ======================# PERSONA RANSOM BOUNDS EXCEPTION #======================#
class PersonaRansomBoundsException(InvalidPersonaException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a designation is outside the range of acceptable Persona ransoms.

    # PARENT:
        *   InvalidPersonaException
        *   BoundsException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_RANSOM_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Ransom is not included in the set of permissible persona ransoms."