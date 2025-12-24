# src/chess/persona/validator/exception/quota.py

"""
Module: chess.persona.validator.exception.quota
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BoundsException
from chess.persona import InvalidPersonaException


__all__ = [
    # ======================# PERSONA QUOTA BOUNDS EXCEPTION #======================#
    "PersonaQuotaBoundsException",
]


# ======================# PERSONA QUOTA BOUNDS EXCEPTION #======================#
class PersonaQuotaBoundsException(InvalidPersonaException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a designation is outside the range of acceptable Persona quotas.

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
    ERROR_CODE = "PERSONA_QUOTA_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Quota is not included in the set of permissible persona quotas."