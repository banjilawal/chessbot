# src/logic/persona/key/lookup/exception/validator.py

"""
Module: logic.persona.key.lookup.exception.work
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from schema.persona import PersonaException
from system import LookupException

__all__ = [
    # ======================# PERSONA_LOOKUP_FAILURE #======================#
    "PersonaLookupFailedException",
]


# ======================# PERSONA_LOOKUP_FAILURE #======================#
class PersonaLookupFailedException(PersonaException, LookupException):
    """
    Role:WorkException, Encapsulation

    Responsibilities:
    1.  Wrap debug exceptions indicating why a rank failed its validation as a Square. The exception chain traces the ultimate source of failure.

    Super Class:
        *   PersonaException
        *   LookupException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PERSONA_LOOKUP_FAILURE"
    MSG = "PersonaLookupProcess failed."

