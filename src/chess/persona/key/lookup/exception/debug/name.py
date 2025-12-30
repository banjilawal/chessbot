# src/chess/persona/validator/exception/name.py

"""
Module: chess.persona.validator.exception.name
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.persona import InvalidPersonaException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# PERSONA NAME BOUNDS EXCEPTION #======================#
    "PersonaNameBoundsException",
]


# ======================# PERSONA NAME BOUNDS EXCEPTION #======================#
class PersonaNameBoundsException(InvalidPersonaException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a name is outside the range of acceptable Persona names.

    # PARENT:
        *   InvalidPersonaException
        *   BoundsException
        *   NameException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Name is not included in the set of permissible persona names."