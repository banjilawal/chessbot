# src/chess/persona/validator/exception/quota.py

"""
Module: chess.persona.validator.exception.quota
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BoundsException
from chess.persona import PersonaException


__all__ = [
    # ======================# PERSONA_QUOTA_BOUNDS EXCEPTION #======================#
    "PersonaQuotaBoundsException",
]


# ======================# PERSONA_QUOTA_BOUNDS EXCEPTION #======================#
class PersonaQuotaBoundsException(PersonaException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a Persona lookup failed because the quota value was not permitted for the Persona
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
    ERROR_CODE = "PERSONA_QUOTA_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "PersonaLookup failed: Target was outside the set of possible Persona quotas."