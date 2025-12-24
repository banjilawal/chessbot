# src/chess/persona/exception.py

"""
Module: chess.persona.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ========================= PERSONA EXCEPTION =========================#
    "PersonaException",
]


# ========================= PERSONA EXCEPTION =========================#
class PersonaException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Persona objects.
    2.  Catchall for conditions which are not covered by lower level Persona exceptions.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PERSONA_ERROR"
    DEFAULT_MESSAGE = "Persona raised an exception."
