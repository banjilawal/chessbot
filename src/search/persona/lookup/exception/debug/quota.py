# src/logic/persona/validation/exception/quota.py

"""
Module: logic.persona.validation.exception.quota
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from system import BoundsException
from catalog.persona import PersonaException


__all__ = [
    # ======================# PERSONA_QUOTA_BOUNDS EXCEPTION #======================#
    "PersonaQuotaBoundsException",
]


# ======================# PERSONA_QUOTA_BOUNDS EXCEPTION #======================#
class PersonaQuotaBoundsException(PersonaException, BoundsException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that a Persona lookup failed because the quota value was not permitted for the Persona
        attribute.

    Super Class:
        *   PersonaException
        *   BoundsException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PERSONA_QUOTA_BOUNDS_EXCEPTION"
    MSG = "PersonaLookupProcess failed: Target was outside the set of possible Persona quotas."