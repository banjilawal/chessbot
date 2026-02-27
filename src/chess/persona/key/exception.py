# src/chess/persona/exception.py

"""
Module: chess.persona.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextException

__all__ = [
    # ======================# PERSONA_KEY EXCEPTION #======================#
    "PersonaKeyException",
]


# ======================# PERSONA_KEY EXCEPTION #======================#
class PersonaKeyException(ContextException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by PersonaContext objects.
    2.  Super for conditions which are not covered by lower level PersonaContext exceptions.

    # PARENT:
        *   PersonaException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PERSONA_KEY_EXCEPTION"
    DEFAULT_ERR_CODE = "PersonaContext raised an exception."