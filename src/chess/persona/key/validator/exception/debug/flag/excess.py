# src/chess/persona/key/validator/exception/flag/excess.py

"""
Module: chess.persona.key.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.persona import InvalidPersonaSuperKeyException

__all__ = [
    # ========================= EXCESSIVE_PERSONA_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessivePersonaSuperKeyFlagsException"
]


# ========================= EXCESSIVE_PERSONA_CONTEXT_FLAG EXCEPTION =========================#
class ExcessivePersonaSuperKeyFlagsException(InvalidPersonaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one PersonaSuperKey flag was enabled. Only one Persona attribute-value tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidPersonaSuperKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_PERSONA_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "Excessive PersonaSuperKey flags were set. Only one PersonaSuperKey flag is allowed."
