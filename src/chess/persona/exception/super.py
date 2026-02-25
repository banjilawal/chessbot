# src/chess/persona/exception.py

"""
Module: chess.persona.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# PERSONA EXCEPTION #======================#
    "PersonaException",
]

from chess.system import SuperClassException


# ======================# PERSONA EXCEPTION #======================#
class PersonaException(SuperClassException):
    """
  # ROLE: DebugException Parent, Exception Chain Layer 0

  # RESPONSIBILITIES:
  1.  Layer-0 of Exception chain which is the Parent of PersonaDebugException

  # PARENT:
      *   SuperClassException

  # PROVIDES:
  None

  # ATTRIBUTES:
  None
  """
    ERR_CODE = "PERSONA_ERROR"
    MSG = "Persona raised an exception."