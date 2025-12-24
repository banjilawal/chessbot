# src/chess/persona/validator/exception/designation.py

"""
Module: chess.persona.validator.exception.designation
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.persona import InvalidPersonaException
from chess.system import BoundsException, NameException


__all__ = [
    # ======================# PERSONA DESIGNATION BOUNDS EXCEPTION #======================#
    "PersonaDesignationBoundsException",
]


# ======================# PERSONA DESIGNATION BOUNDS EXCEPTION #======================#
class PersonaDesignationBoundsException(InvalidPersonaException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a designation is outside the range of acceptable Persona designations.

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
    ERROR_CODE = "PERSONA_DESIGNATION_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Designation is not included in the set of permissible persona designations."