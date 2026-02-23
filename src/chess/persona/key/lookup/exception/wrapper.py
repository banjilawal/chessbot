# src/chess/persona/key/lookup/exception/wrapper.py

"""
Module: chess.persona.key.lookup.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.persona import PersonaException
from chess.system import LookupException

__all__ = [
    # ======================# PERSONA_LOOKUP_FAILURE #======================#
    "PersonaLookupFailedException",
]


# ======================# PERSONA_LOOKUP_FAILURE #======================#
class PersonaLookupFailedException(PersonaException, LookupException):
    """
    # ROLE: WrapperException, Encapsulation

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Square. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   PersonaException
        *   LookupException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_LOOKUP_FAILURE"
    DEFAULT_MESSAGE = "PersonaLookup failed."

