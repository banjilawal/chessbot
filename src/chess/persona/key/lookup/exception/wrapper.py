# src/chess/persona/key/lookup/exception/wrapper.py

"""
Module: chess.persona.key.lookup.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.persona import PersonaException
from chess.system import LookupFailedException

__all__ = [
    # ======================# PERSONA_LOOKUP_FAILURE EXCEPTION #======================#
    "PersonaLookupFailedException",
]


# ======================# PERSONA_LOOKUP_FAILURE EXCEPTION #======================#
class PersonaLookupFailedException(PersonaException, LookupFailedException):
    """
    # ROLE: ExceptionWrapper, Encapsulation

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a Square. The encapsulated
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   PersonaException
        *   LookupFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_LOOKUP_FAILURE"
    DEFAULT_MESSAGE = "PersonaLookup failed."

